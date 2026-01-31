EXPENSES_FILE = "data/expenses_data.json"
WAGES_FILE = "data/wages_data.json"

import json
import os


def load_data(file_path):
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []


def save_data(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def get_float_input(prompt):
    value = input(prompt)
    try:
        return float(value)
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None


def get_currency_input(prompt):
    currency = input(prompt).upper()

    if len(currency) != 3 or not currency.isalpha():
        print("Invalid currency code. Please enter a 3-letter code (e.g. GBP, USD).")
        return None
    
    return currency
