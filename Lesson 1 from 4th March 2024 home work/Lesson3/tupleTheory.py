# myList = [1, 2, 3, 4]
# print(type(myList))

# tttuple = 1, 2, 3, 4
# print(type(tttuple))

# #tuples cannot be changes unlike the lists
# myTuple = "Darinka", 26, True

# name, age, isHungry = myTuple
# print(isHungry)

# mySet = set() # similar is to lists' [] / mnoziny

# mySet.add("Darinka")
# mySet.add("Snouma")
# mySet.add("Snouma")
# print(mySet)

# myDictionary = {}
# print(type(myDictionary))

#tea pot = title, 899 - price, True = inStock
# things = {"title": "tea pot", 
#           "price": 899, 
#           "inStock": True}

# print(things["title"])
# #if the key isn't found, the program will add the new key in the dictionary
# things["weight"] = 0.5

# print(things["weight"])

# things["weight"] = 1
# #if the key is found, the program will change the value in the key
# print(things["weight"])

# Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka z daného předmětu. 
# Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis). Vypiš obsah slovníku pomocí funkce print().

# schoolReport = {"Czech Language": 1, "Math": 3, "History": 5}
# print(schoolReport["Math"])

# Vydavatel detektivek si eviduje prodané kusy u jednotlivých knih. V následujícím slovníku najdeš tři knihy a u každé z nich je počet prodaných kusů.

# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }

# sales["Noc, která mě zabila"] = 0

# print(sales)

# sales["Vrah zavolá v deset"] += 100

# print(sales)


# tombola = {
#     7: "Láhev kvalitního vína Château Headache",
#     15: "Pytel brambor z místního družstva",
#     23: "Čokoládový dort",
#     47: "Kniha o historii města",
#     55: "Šiška salámu",
#     67: "Vyhlídkový let balónem",
#     79: "Moderní televizor",
#     91: "Roční předplatné městského zpravodaje",
#     93: "Společenská hra Sázky a dostihy",
# }

# ticketNumber = int(input("ZAdejte cislo listku: "))
# if ticketNumber in tombola:
#     print(f"Vyhrali jste {tombola[ticketNumber]}")
# else:
#     print("Bohužel nevyhráváš nic.")


# Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, že každý z hostů bude mít speciální heslo, které je platné jen pro něj. 
# Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, a pokud tam je, 
# zeptá se ho na heslo a zkontroluje jeho správnost. 
# Hostu na seznamu, který zadá správné heslo, vypíše program text: "Smíš vstoupit."
# passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

# name = input("Type in your name: ")
# if name in passwords:
#     passwordUserInput = input("Type in your password: ")
#     if passwordUserInput in passwords[name]:
#         print("You are very welcome.")
#     else:
#         print("We are calling police.")
# else:
#     print("You are at a wrong party.")

# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }
# totalSales = 0
# for bookName in sales:
#     print(bookName)

# for bookName, prints in sales.items():
#     totalSales += prints
#     print(bookName, prints)

# print(totalSales)
# print(sales.values())
# print(sales.keys())
# print(sales)

school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}

# totalScore = 0
# for subjectName, score in school_report.items():
#     totalScore += score

# average = totalScore / len(school_report)
# print(average)

# totalScoreShort = sum(school_report.values())
# average = totalScoreShort / len(school_report)
# print(average)

# average = sum(school_report.values()) / len(school_report)
# print(average)

# Uprav program, aby vypsal všechny předměty, ve kterých získal student známku 1.

# for subject, score in school_report.items():
#     if score == 1:
#         print(subject)


books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

totalPagesRead = 0

for item in books:
    print(item["pages"])

# pocet stran u hodnoceni nad 8