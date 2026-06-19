import json
import os
import sys
from datetime import datetime

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as file:
            json.dump([], file)

    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(description, amount):
    expenses = load_expenses()

    new_id = 1
    if expenses:
        new_id = max(expense["id"] for expense in expenses) + 1

    expense = {
        "id": new_id,
        "description": description,
        "amount": float(amount),
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    expenses.append(expense)
    save_expenses(expenses)

    print(f"Expense added successfully (ID: {new_id})")


def update_expense(expense_id, description, amount):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expense["description"] = description
            expense["amount"] = float(amount)

            save_expenses(expenses)
            print("Expense updated successfully")
            return

    print("Expense not found")


def delete_expense(expense_id):
    expenses = load_expenses()

    for expense in expenses:
        if expense["id"] == expense_id:
            expenses.remove(expense)
            save_expenses(expenses)
            print("Expense deleted successfully")
            return

    print("Expense not found")


def list_expenses():
    expenses = load_expenses()

    if not expenses:
        print("No expenses found")
        return

    print("-" * 60)
    print(f"{'ID':<5}{'DATE':<15}{'DESCRIPTION':<25}{'AMOUNT'}")
    print("-" * 60)

    for expense in expenses:
        print(
            f"{expense['id']:<5}"
            f"{expense['date']:<15}"
            f"{expense['description']:<25}"
            f"{expense['amount']}"
        )


def summary_expenses():
    expenses = load_expenses()

    total = sum(expense["amount"] for expense in expenses)

    print(f"Total expenses: ₹{total}")


def summary_by_month(month):
    expenses = load_expenses()

    total = 0

    for expense in expenses:
        expense_month = datetime.strptime(
            expense["date"], "%Y-%m-%d"
        ).month

        if expense_month == month:
            total += expense["amount"]

    print(f"Total expenses for month {month}: ₹{total}")


def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print(
            'python expense.py add "Description" Amount'
        )
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 4:
            print(
                'Usage: python expense.py add "Description" Amount'
            )
            return

        add_expense(sys.argv[2], sys.argv[3])

    elif command == "update":
        if len(sys.argv) != 5:
            print(
                'Usage: python expense.py update ID "Description" Amount'
            )
            return

        update_expense(
            int(sys.argv[2]),
            sys.argv[3],
            sys.argv[4]
        )

    elif command == "delete":
        if len(sys.argv) != 3:
            print(
                "Usage: python expense.py delete ID"
            )
            return

        delete_expense(int(sys.argv[2]))

    elif command == "list":
        list_expenses()

    elif command == "summary":
        if len(sys.argv) == 2:
            summary_expenses()
        elif len(sys.argv) == 3:
            summary_by_month(int(sys.argv[2]))
        else:
            print(
                "Usage: python expense.py summary [month]"
            )

    else:
        print("Invalid command")


if __name__ == "__main__":
    main()

