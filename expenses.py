def add_expense():

    # 1. Ask user for amount
    amount = input("Enter expense amount: ")
    try:
        amount = float(amount)
    except:
        print("Invalid amount. Please enter a number.")
        return
    print(f"Amount entered: {amount}")

    # 2. Ask user for durrency
    currency = input("Enter currency (e.g., USD, GBP): ")
    print(f"Currency entered: {currency}")
    
    # 3. Ask user for category
    # 4. Ask user for date (optional)
    # 5. Store details in a dictionary or database
    #6. Print confirmation message



def view_expenses():
    print("View expenses — not implemented yet")
