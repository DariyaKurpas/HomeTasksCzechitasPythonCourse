import json

path = r"C:\Users\dasha\HomeTasksCzechitasPythonCourse\Lesson11\absolventi.json"

with open(path, encoding="utf-8") as file:
    absolvents = json.load(file)

print(absolvents)

# for i in absolvents:
#     print(i["dochazka"])

# hours = {"Mon": 8, "Tue": 7, "Wed": 6, "Thu": 10, "Fri": 4}

# with open("C:\Users\dasha\HomeTasksCzechitasPythonCourse\Lesson11\py_to_json.json", mode="w", encoding="urf-8") as file:
#     json.dump(hours, file)

# data = {"řeřicha": "Česká Třebová"}

# with open("new_file.json", mode="w", encoding="utf-8") as file:
#     json.dump(data, file, ensure_ascii=False)

# with open("Lesson11\zavod.json", encoding="utf-8") as file:
#     runners = json.load(file)
# print(runners[0])
# print(runners[0]["jmeno"])