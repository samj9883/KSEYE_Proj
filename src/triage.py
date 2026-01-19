import json
from datetime import datetime, timedelta, timezone

import re
from typing import Tuple


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

#print(print_all_overdue())

# --------------------------------------------------------------------------------------------------------


# Ordered rules: first match wins (most specific first)
_CATEGORY_RULES: list[tuple[str, re.Pattern]] = [
    ("EMAIL_CHANGE", re.compile(r"\b(email|e-mail)\b.*\b(incorrect|wrong|amend|update|change)\b", re.I)),
    ("NEW_STARTER_ACCESS", re.compile(r"\bnew starter\b|\bonboard(ing)?\b|\bneeds system access\b", re.I)),
    ("PRICING_MATRIX_HELP", re.compile(r"\bpricing matrix\b|\bprice for (their )?enquiry\b|\bprice (a )?case\b", re.I)),
    ("TEMPLATE_LETTER", re.compile(r"\btemplate letter\b|\bletter template\b|\bfill in the blanks\b|\bauto-?fill\b", re.I)),
    ("APPLICATION_INFO", re.compile(r"\bapplication\b\s*[A-Z]{3}\d+\b|\bwhat information\b.*\bapplication\b", re.I)),
    ("LENDING_CRITERIA", re.compile(r"\blending criteria\b|\blatest criteria\b", re.I)),
    ("FUNDING_CALCULATOR", re.compile(r"\bfunding calculator\b|\buse the.*calculator\b", re.I)),
]

def categorise_ticket(message: str) -> str:
    """
    Categorise a ticket based on simple, explainable keyword rules.

    Args:
        message (str): The raw ticket message text.

    Returns:
        str: Category label such as EMAIL_CHANGE, APPLICATION_INFO, etc.
    """
    if not message or not message.strip():
        return "GENERAL"

    for category, pattern in _CATEGORY_RULES:
        if pattern.search(message):
            return category

    return "GENERAL"


def print_categories(filter: str):

    if filter == "ALL":
        for ticket in tickets:
            print(f"Ticket {ticket.get('id')} category: {categorise_ticket(ticket.get('message'))}")

    else:
         for ticket in tickets:
            if categorise_ticket(ticket.get('message')) == filter:
                print(f"Ticket {ticket.get('id')} category: {categorise_ticket(ticket.get('message'))}")


    
    
print_categories("EMAIL_CHANGE")