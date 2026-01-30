from utils import(
EXPENSES_FILE,
load_data,
save_data,
get_float_input,
get_currency_input
)

expenses = load_data(EXPENSES_FILE)

def add_expense(): # collect expense details from user

    # 1. Ask user for amount
    amount = get_float_input("Enter expense amount: ")
    if amount is None:
        return
    
    print(f"Amount entered: {amount}")

    # 2. Ask user for durrency
    currency = get_currency_input("Enter currency (GBP, USD, EUR, etc.): ")
    if currency is None:
        return
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

    save_data(EXPENSES_FILE, expenses)


def view_expenses():

    if not expenses:
        print("No expenses recorded yet.")
        return
    
    for expense in expenses:
        print(f"{expense['amount']} {expense['currency']} - {expense['category']} on {expense['date']}")
