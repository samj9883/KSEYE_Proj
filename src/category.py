from typing import Any, Dict, List, Tuple
import re

# Ordered rules: first match wins (most specific first)
_CATEGORY_RULES: List[Tuple[str, re.Pattern]] = [
    ("EMAIL_CHANGE", re.compile(r"\b(email|e-mail)\b.*\b(incorrect|wrong|amend|update|change)\b", re.I)),
    ("NEW_STARTER_ACCESS", re.compile(r"\bnew starter\b|\bonboard(ing)?\b|\bneeds system access\b", re.I)),
    ("PRICING_MATRIX_HELP", re.compile(r"\bpricing matrix\b|\bprice for (their )?enquiry\b|\bprice (a )?case\b", re.I)),
    ("TEMPLATE_LETTER", re.compile(r"\btemplate letter\b|\bletter template\b|\bfill in the blanks\b|\bauto-?fill\b", re.I)),
    ("APPLICATION_INFO", re.compile(r"\bapplication\b\s*[A-Z]{3}\d+\b|\bwhat information\b.*\bapplication\b", re.I)),
    ("LENDING_CRITERIA", re.compile(r"\blending criteria\b|\blatest criteria\b", re.I)),
    ("FUNDING_CALCULATOR", re.compile(r"\bfunding calculator\b|\buse the.*calculator\b", re.I)),
]

def available_categories() -> List[str]:
    """
    Returns the list of available category filters including ALL.
    """
    cats = [name for name, _ in _CATEGORY_RULES]
    return ["ALL"] + cats + ["GENERAL"]


def categorise_ticket(message: str) -> str:
    """
    Categorise a ticket based on simple, explainable keyword rules.
    """
    if not message or not message.strip():
        return "GENERAL"

    for category, pattern in _CATEGORY_RULES:
        if pattern.search(message):
            return category

    return "GENERAL"


def print_categories(tickets: List[Dict[str, Any]], filter_value: str) -> None:
    """
    Prints ticket categories. If filter_value == 'ALL', prints all.
    Otherwise prints only tickets matching the category.
    """
    filter_value = filter_value.upper()
    print("-" * 40)

    for ticket in tickets:
        ticket_id = ticket.get("id", "UNKNOWN")
        message = ticket.get("message", "")
        time = ticket.get("created_at", "")

        category = categorise_ticket(message)

        if filter_value == "ALL" or category == filter_value:
            print(f"Ticket {ticket_id} category: {category}")
            print(f"Received At: {time}")
            print(f"Message: {message}")
            print("-" * 40)
            
            
