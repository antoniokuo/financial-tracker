from utils import(
EXPENSES_FILE,
load_data,
save_data,
get_float_input,
get_currency_input,
calculate_totals_by_currency
)

_expenses = load_data(EXPENSES_FILE)

def add_expense(): # collect expense details from user

    # 1. Ask user for amount
    amount = get_float_input("Enter expense amount: ")

    # 2. Ask user for durrency
    currency = get_currency_input("Enter currency (GBP, USD, EUR, etc.): ")

    # 3. Ask user for category
    category = input("Enter category (press enter to skip): ")
    if category == "":
        category = "Miscellaneous"

    # 4. Ask user for date (optional)
    date = input("Enter date (press enter to skip): ")
    if date == "":
        date = "Not specified"

    # 5. Store details in a dictionary
    expense = {
        "amount": amount,
        "currency": currency,
        "category": category,
        "date": date
    }
    _expenses.append(expense)

    # 6. Print confirmation message
    print("Expense added successfully!")
    print(f"Expense added: {amount} {currency} for {category} on {date}")

    save_data(EXPENSES_FILE, _expenses)


def view_expenses():

    if not _expenses:
        print("No expenses recorded yet.")
        return
    
    for expense in _expenses:
        print(f"{expense['amount']} {expense['currency']} - {expense['category']} on {expense['date']}")

    totals = {}

    for expense in _expenses:
        currency = expense['currency']
        amount = expense['amount']

        if currency not in totals:
            totals[currency] = 0
        
        totals[currency] += amount

    print("\nTotal Expenses:")
    for currency, total in totals.items():
        print(f"{currency}: {total}")
    

def get_expense_totals():
    return calculate_totals_by_currency(
        _expenses,
        lambda expense: expense['amount']
    )
