import json

finishers = []

runners = r"C:\Users\dasha\HomeTasksCzechitasPythonCourse\Lesson11\zavod.json"

with open(runners, encoding="utf-8") as file:
    all_runners = json.load(file)

print(all_runners)

for person in all_runners:
    print(person["jmeno"], person["casy"])
    

# print(finishers)