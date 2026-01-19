import json

with open("data/tickets.json", "r", encoding="utf-8") as file:
    tickets = json.load(file)



for ticket in tickets:
    ticket_id = ticket.get("id", "UNKNOWN")
    created_at = ticket.get("created_at","UNKNOWN")
    channel = ticket.get("channel", "UNKNOWN")
    message = ticket.get("message", "")

    print(f"[{ticket_id}], Created At: {created_at} ({channel}) {message}")

    print("-" * 40)


