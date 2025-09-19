exchange_rates = {
    'USD': 0.012,
    'EUR': 0.011,
    'JPY': 1.75,
    'INR': 1.0
}
def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("Unsupported currency.")
        return
    amount_in_inr = amount / exchange_rates[from_currency]
    converted = amount_in_inr * exchange_rates[to_currency]
    print(f"{amount} {from_currency} = {converted:.2f} {to_currency}")
amount = float(input("Enter amount: "))
from_curr = input("From currency (e.g., USD, EUR, INR): ").upper()
to_curr = input("To currency (e.g., USD, EUR, INR): ").upper()

convert_currency(amount, from_curr, to_curr)
'''op
Enter amount: 569
From currency (e.g., USD, EUR, INR): usd
To currency (e.g., USD, EUR, INR): inr
569.0 USD = 47416.67 INR
'''
