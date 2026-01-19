# overdue.py

from datetime import datetime, timedelta, timezone
from typing import Any, Dict, List


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


def print_all_overdue(tickets: List[Dict[str, Any]]) -> None:
    """
    Prints all tickets that have exceeded their SLA.
    """
    now = datetime.now(timezone.utc)

    for ticket in tickets:
        created_at_str = ticket.get("created_at")
        sla_hours = int(ticket.get("sla_hours", 0))

        if not created_at_str:
            continue  # skip invalid records safely

        created_at = datetime.fromisoformat(
            created_at_str.replace("Z", "+00:00")
        )

        if is_overdue(created_at, sla_hours, now):
            print(f"OVERDUE: {ticket.get('id', 'UNKNOWN')}")
            print(f"  Created at: {created_at}")
            print(f"  SLA hours: {sla_hours}")
            print(f"  Message: {ticket.get('message', '')}")
            print("-" * 40)
