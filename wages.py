from utils import(
    WAGES_FILE,
    load_data,
    save_data,
    get_float_input,
    get_currency_input,
    calculate_totals_by_currency
)

_wages = load_data(WAGES_FILE)

def add_work_hours():
    # 1. Ask user for hours worked
    hours = get_float_input("Enter work hours: ")
    if hours is None:
        return
    
    print(f"Work hours entered: {hours}")

    # 2. Ask user for hourly rate
    rate = get_float_input("Enter hourly rate: ")
    if rate is None:
        return
    
    print(f"Hourly rate entered: {rate}")

    # 3. Ask user for currency
    currency = get_currency_input("Enter currency (GBP, USD, EUR, etc.): ")
    if currency is None:
        return
    
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
    _wages.append(wage)
    print(_wages)

    # 6. Print confirmation message
    print("Work hours added successfully!")
    print(f"Work hours added: {hours} hours at {rate} {currency} on date {date}")

    save_data(WAGES_FILE, _wages)


def view_wages():

    if not _wages:
        print("No work hours recorded yet.")
        return
    
    for wage in _wages:
        print(f"{wage['hours']} hours at {wage['rate']} {wage['currency']} on {wage['date']}")

    totals = {}

    for wage in _wages:
        currency = wage['currency']
        total_pay = wage['hours'] * wage['rate']

        if currency not in totals:
            totals[currency] = 0

        totals[currency] += total_pay

    print("\nTotal Wages:")
    for currency, total in totals.items():
        print(f"{currency}: {total}")
    

def get_wage_totals():
    return calculate_totals_by_currency(
        _wages,
        lambda wage: wage['hours'] * wage['rate']
    )
