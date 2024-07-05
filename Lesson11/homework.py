import json

# path = r"C:\Users\dasha\HomeTasksCzechitasPythonCourse\Lesson11\homework1.json"

# with open(path, encoding="utf-8") as file:
#     new_student = json.load(file)
#     for one_student in new_student:
#         print(one_student)


# hours = {'po': 8, 'ut': 7, 'st': 6, 'ct': 7, 'pa': 8}
# with open("working_hours", mode="a", encoding="utf-8") as file:
#     json.dump(hours, file)

# data = {"řeřicha": "Česká Třebová"}

# with open("gardener.json", mode="a", encoding="utf-8") as file:
#     json.dump(data, file, ensure_ascii=False)

path = r"C:\Users\dasha\HomeTasksCzechitasPythonCourse\Lesson11\zavod.json"
with open(path, encoding="utf-8") as file:
    runners = json.load(file)
    winner = runners[0]
    winner_time = winner["casy"]["2.kolo"]
print(winner_time)