from zendesk_loader import load_from_zendesk

data = load_from_zendesk()

print(len(data))
print(data[0])
