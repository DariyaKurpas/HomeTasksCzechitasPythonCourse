from forex_python.converter import CurrencyRates

c = CurrencyRates()
rates = c.get_rates("CZK")
# for key, value in rates.items():
#     rate = 1 / value
#     print(f"1 {key} = {round(rate, 2)}")

currency_list = ["GBP", "EUR", "USD"]
for key, value in rates.items():
    if key in currency_list:
        rate = 1 / value
        print(f"1 {key} = {round(rate, 2)}")