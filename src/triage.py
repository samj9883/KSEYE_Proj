import json

with open("data/tickets.json", "r", encoding="utf-8") as file:
    tickets = json.load(file)

for ticket in tickets:
    print(f"ID: {ticket['id']}")
    print(f"Created At: {ticket['created_at']}")
    print(f"Channel: {ticket['channel']}")
    print(f"Message: {ticket['message']}")
    print("-" * 40)
