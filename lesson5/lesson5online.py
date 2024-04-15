import statistics
# velikonoce = {"datum": "01.04.2024",
#               "klic": "hondoty",
#               "klic": "hondoty",
#               "symboly": ["vajicko", "pomlazka", "beranek"],
#               "pocasi": {"teplota": "20", 
#                          "oblacnost": "jasno"},
#               "dalsi slovnik": {"klic": "hondota"}
#               }

# print(velikonoce["symboly"][1])
# print(velikonoce["pocasi"]["teplota"])
# for item, value in velikonoce.items():
#     for item["pocasi"], value in item.items():
#         print(value)

# velikonoce["pocasi"].update({"srazky": "zadne"})
# print(velikonoce["pocasi"])

# velikonoce["symboly"].append("kuratko")
# print(velikonoce["symboly"])

# school_report = {
#     "Český jazyk": 1,
#     "Anglický jazyk": 1,
#     "Matematika": 1,
#     "Přírodopis": 2,
#     "Dějepis": 1,
#     "Fyzika": 2,
#     "Hudební výchova": 4,
#     "Výtvarná výchova": 2,
#     "Tělesná výchova": 3,
#     "Chemie": 4,
# }

# Napiš program, který spočte průměrnou známku ze všech předmětů.

# average = sum(school_report.values()) / len(school_report)
# print(average)

# average = sum(value for item, value in school_report.items()) / len(school_report)
# print(average)

# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.



# subjectsWith1 = []

# for subject, value in school_report.items():
#     if value == 1:
#         subjectsWith1.append(subject)

# print(subjectsWith1)

# allSubjectsWith1 = list(filter(lambda y: y == 1, school_report))
# print(allSubjectsWith1)


myList = ["Darinka", "Filip", "Snouma", "Mexican", "Bob", "Kevin", "Timmy"]

namesWithA = list(filter(lambda containsAO: "a" in containsAO.lower() and "o" in containsAO.lower(), myList))
print(namesWithA)