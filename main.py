from expenses import add_expense, view_expenses
from wages import add_work_hours, view_wages


def show_menu():
    print("\nFinancial Tracker")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Add Work Hours")
    print("4. View Wages")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Select an option (1-5): ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            add_work_hours()
        elif choice == "4":
            view_wages()
        elif choice == "5":
            print("Exiting Financial Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
