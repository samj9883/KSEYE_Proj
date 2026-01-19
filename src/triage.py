import json
from typing import Any, Dict, List

from overdue import print_all_overdue
from category import print_categories, available_categories


def load_tickets(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def prompt_menu_choice() -> str:
    print("\n=== Ops Ticket Search ===")
    print("1) Timeline search (overdue tickets)")
    print("2) Category search")
    print("3) Exit")
    return input("Choose an option (1-3): ").strip()


def prompt_category_choice(categories: List[str]) -> str:
    print("\nAvailable categories:")
    for i, cat in enumerate(categories, start=1):
        print(f"{i}) {cat}")

    while True:
        choice = input(f"Select a category (1-{len(categories)}): ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(categories):
                return categories[idx - 1]

        print("Invalid selection. Please try again.")


def main() -> None:
    tickets = load_tickets("data/tickets.json")

    while True:
        choice = prompt_menu_choice()

        if choice == "1":
            print("\n--- Overdue Tickets ---")
            print_all_overdue(tickets)

        elif choice == "2":
            cats = available_categories()
            selected = prompt_category_choice(cats)

            print(f"\n--- Tickets in Category: {selected} ---")
            print_categories(tickets, selected)

        elif choice == "3":
            print("Goodbye.")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")


if __name__ == "__main__":
    main()
