from expenses import add_expense, view_expenses, get_expense_totals, load_expenses
from wages import add_work_hours, view_wages, get_wage_totals, load_wages


def show_menu():
    print("\nFinancial Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Add Work Hours")
    print("4. View Wages")
    print("5. View Net Balance")
    print("6. Exit")


def main():
    load_expenses()
    load_wages()

    while True:
        show_menu()
        choice = input("Select an option (1-6): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            add_work_hours()
        elif choice == "4":
            view_wages()
        elif choice == "5":
            expenses = get_expense_totals()
            wages = get_wage_totals()
            currencies = set(expenses.keys()) | set(wages.keys())
            
            print("\nNet Balance:")
            for currency in currencies:
                total_expenses = expenses.get(currency, 0)
                total_wages = wages.get(currency, 0)
                net_balance = total_wages - total_expenses

                print(f"\n{currency}:")
                print(f"  Wages: {total_wages}")
                print(f"  Expenses: {total_expenses}")
                print(f"  Net Balance: {net_balance}")

        elif choice == "6":
            print("Exiting Financial Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
