import math
import statistics

# number = 3.14

# #funkce ceil() a floor()

# print(math.floor(number))

# # print(number.__floor__()) nepouzivat
# print(math.ceil(number))

# print(statistics.mean([1, 10])) # mean = prumer = average

# number = 5.6457

# print(math.floor(number))
# print(math.ceil(number))
# print(round(number, 2))

class lesson:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade


# school_report = [
#     ["Český jazyk", 1],
#     ["Anglický jazyk", 1],
#     ["Matematika", 1],
#     ["Přírodopis", 2],
#     ["Dějepis", 1],
#     ["Fyzika", 2],
#     ["Hudební výchova", 4],
#     ["Výtvarná výchova", 2],
#     ["Tělesná výchova", 3],
#     ["Chemie", 4],
# ]

myEnglishLesson = lesson("EN", 1)

school_report = [
    lesson("Cesky Jazyk", 5)
]

importantSubj = []

for lesson in school_report:
    
    # importantSubj.append()
    if lesson.name == "Český jazyk" or lesson[0] == "Anglický jazyk" or lesson[0] == "Matematika" or lesson[0] == "Fyzika":
        importantSubj.append(lesson.grade)

print(statistics.mean(importantSubj))

