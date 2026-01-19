import json
from datetime import datetime, timedelta, timezone


with open("data/tickets.json", "r", encoding="utf-8") as file:
    tickets = json.load(file)


# SLA and created time based overdue logic

# SLA Comparison to current time
now = datetime.now(timezone.utc)


def is_overdue(created_at: datetime, sla_hours: int, now: datetime) -> bool:
    """
    Determines whether a request has exceeded its SLA.

    Args:
        created_at (datetime): Time the request was created (UTC).
        sla_hours (int): Allowed time window in hours.
        now (datetime): Current time (UTC).

    Returns:
        bool: True if the request is overdue, otherwise False.
    """
    return now > created_at + timedelta(hours=sla_hours)

def print_all_overdue():

    for ticket in tickets:
        created_at_str = ticket.get("created_at")
        sla_hours = ticket.get("sla_hours", 0)

        # Convert ISO string to datetime (handle Z)
        created_at = datetime.fromisoformat(
            created_at_str.replace("Z", "+00:00")
        )

        if is_overdue(created_at, sla_hours, now):
            print(f"OVERDUE: {ticket.get('id')}")
            print(f"  Created at: {created_at}")
            print(f"  SLA hours: {sla_hours}")
            print(f"  Message: {ticket.get('message')}")
            print("-" * 40)

print(print_all_overdue())

# --------------------------------------------------------------------------------------------------------