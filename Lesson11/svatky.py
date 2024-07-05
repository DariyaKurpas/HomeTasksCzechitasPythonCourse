import requests

path = "https://svatky.adresa.info/json?date="

day = input("Type in the day in the format DD:\n")
month = input("Type in the month in the format MM:\n")

name_of_the_day = path + day + month
response = requests.get(name_of_the_day)

# data = response.json()

print(response)