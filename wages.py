import json
import os
from utils import WAGES_FILE

wages = [] # empty list to store wages
if os.path.exists(WAGES_FILE):
    with open(WAGES_FILE, "r") as file:
        wages = json.load(file)

def add_work_hours():
    # 1. Ask user for hours worked
    hours = input("Enter work hours: ")
    try:
        hours = float(hours)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    print(f"Work hours entered: {hours}")

    # 2. Ask user for hourly rate
    rate = input("Enter hourly rate: ")
    try:
        rate = float(rate)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return
    print(f"Hourly rate entered: {rate}")

    # 3. Ask user for currency
    currency = input("Enter currency (e.g., USD, GBP): ")
    print(f"Currency entered: {currency}")

    # 4. Ask user for date (optional)
    date = input("Enter date (press enter to skip): ")
    if date == "":
        date = "not specified"
    print(f"Date entered: {date}")

    # 5. Store details in a dictionary
    wage = {
        "hours": hours,
        "rate": rate,
        "currency": currency,
        "date": date
    }
    wages.append(wage)
    print(wages)

    # 6. Print confirmation message
    print("Work hours added successfully!")
    print(f"Work hours added: {hours} hours at {rate} {currency} on date {date}")

    with open(WAGES_FILE, "w") as file:
        json.dump(wages, file)

def view_wages():

    if not wages:
        print("No work hours recorded yet.")
        return
    
    for wage in wages:
        print(f"{wage['hours']} hours at {wage['rate']} {wage['currency']} on {wage['date']}")
