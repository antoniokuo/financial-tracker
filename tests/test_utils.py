from utils import calculate_totals_by_currency

def test_calculate_totals_by_currency_for_expenses():
    expenses = [
        {"amount": 10, "currency": "USD"},
        {"amount": 5, "currency": "USD"},
        {"amount": 20, "currency": "GBP"},
    ]

    totals = calculate_totals_by_currency(
        expenses,
        lambda expense: expense['amount']
    )

    assert totals == {
        "USD": 15,
        "GBP": 20
    }