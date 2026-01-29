import json
import os

expenses = [] # empty list to store expenses
if os.path.exists("data/expenses_data.json"):
    with open("data/expenses_data.json", "r") as file:
        expenses = json.load(file)

def add_expense(): # collect expense details from user

    # 1. Ask user for amount
    amount = input("Enter expense amount: ")
    try:
        amount = float(amount)
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return
    print(f"Amount entered: {amount}")

    # 2. Ask user for durrency
    currency = input("Enter currency (e.g., USD, GBP): ")
    print(f"Currency entered: {currency}")

    # 3. Ask user for category
    category = input("Enter category (press enter to skip): ")
    if category == "":
        category = "Miscellaneous"
    print(f"{amount}, {currency}, {category}")

    # 4. Ask user for date (optional)
    date = input("Enter date (press enter to skip): ")
    if date == "":
        date = "Not specified"
    print(f"{amount}, {currency}, {category}, {date}")

    # 5. Store details in a dictionary
    expense = {
        "amount": amount,
        "currency": currency,
        "category": category,
        "date": date
    }
    expenses.append(expense)
    print(expenses)

    # 6. Print confirmation message
    print("Expense added successfully!")
    print(f"Expense added: {amount} {currency} for {category} on {date}")

    with open("data/expenses_data.json", "w") as file:
        json.dump(expenses, file)

def view_expenses():

    if not expenses:
        print("No expenses recorded yet.")
        return
    
    for expense in expenses:
        print(f"{expense['amount']} {expense['currency']} - {expense['category']} on {expense['date']}")
