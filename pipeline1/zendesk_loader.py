import os
import requests
import time
from dotenv import load_dotenv

load_dotenv()

SUBDOMAIN = os.getenv("ZENDESK_SUBDOMAIN")
EMAIL = os.getenv("ZENDESK_EMAIL")
API_TOKEN = os.getenv("ZENDESK_API_TOKEN")

BASE_URL = f"https://{SUBDOMAIN}.zendesk.com/api/v2"
AUTH = (f"{EMAIL}/token", API_TOKEN)

RATE_SLEEP = 0.2


def fetch_all_tickets():
    tickets = []
    url = f"{BASE_URL}/tickets.json?page[size]=100"

    while url:
        response = requests.get(url, auth=AUTH)

        if response.status_code != 200:
            raise Exception(f"Zendesk error: {response.text}")

        data = response.json()
        tickets.extend(data["tickets"])
        url = data["links"]["next"]

        time.sleep(RATE_SLEEP)

    return tickets


def fetch_ticket_comments(ticket_id):
    url = f"{BASE_URL}/tickets/{ticket_id}/comments.json"
    response = requests.get(url, auth=AUTH)

    if response.status_code != 200:
        raise Exception(f"Comments error: {response.text}")

    return response.json()["comments"]


def build_conversation(ticket):
    comments = fetch_ticket_comments(ticket["id"])
    requester_id = ticket["requester_id"]

    convo = []

    for c in comments:
        role = "CUSTOMER" if c["author_id"] == requester_id else "AGENT"
        convo.append(f"{role}: {c['body']}")

    return "\n".join(convo)


def load_from_zendesk():
    raw_tickets = fetch_all_tickets()
    records = []

    for t in raw_tickets:
        conversation = build_conversation(t)

        records.append({
            "ticket_id": str(t["id"]),
            "conversation": conversation,
            "timestamp": t["created_at"],
            "status": t["status"]
        })

    return records
