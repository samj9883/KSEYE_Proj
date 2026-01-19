import json
from typing import Any, Dict, List

from overdue import print_all_overdue
from category import print_categories


def load_tickets(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)




def main() -> None:
    tickets = load_tickets("data/tickets.json")

    # Print overdue tickets
    print_all_overdue(tickets)

    # Print categories (examples)
    print_categories(tickets, "ALL")
    # print_categories(tickets, "EMAIL_CHANGE")


if __name__ == "__main__":
    main()
