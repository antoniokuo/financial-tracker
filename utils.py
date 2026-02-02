EXPENSES_FILE = "data/expenses_data.json"
WAGES_FILE = "data/wages_data.json"

import json
import os

from typing import List, Dict, Any, Optional


def load_data(file_path: str) -> List[Dict[str, Any]]:
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    return []


def save_data(file_path: str, data: list) -> None:
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


def get_float_input(prompt: str) -> float:
    while True:
        value = input(prompt)
        try:
            return float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_currency_input(prompt: str) -> str:
    while True:
        currency = input(prompt).upper()

        if len(currency) == 3 and currency.isalpha():
            return currency
        
        print("Invalid currency code. Please enter a 3-letter code (e.g. GBP, USD, EUR).") 

def calculate_totals_by_currency(items, amount_fn):
    totals = {}

    for item in items:
        currency = item['currency']
        amount = amount_fn(item)

        if currency not in totals:
            totals[currency] = 0
        
        totals[currency] += amount
    
    return totals