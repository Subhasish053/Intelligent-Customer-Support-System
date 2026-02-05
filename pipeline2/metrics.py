import random

def calculate_metrics():

    avg_manual_time = 10  # minutes per ticket
    ai_time = 2           # minutes with AI

    time_saved = avg_manual_time - ai_time

    cost_per_minute = 0.5  # assume $0.5 per minute

    cost_saved = time_saved * cost_per_minute

    return {
        "time_saved_minutes": time_saved,
        "cost_saved_dollars": cost_saved,
        "tickets_processed": random.randint(100, 500),
        "escalated_cases": random.randint(5, 30)
    }
