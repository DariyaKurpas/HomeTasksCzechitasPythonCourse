import math

# cookies_count = (1, 2, 4, 1, 6, 0, 1)
# print(type(cookies_count))

# item = "Čajová konvička s hrnky", 899, True

# title, price, in_stock = item

# print(title)
# print(price)
# print(in_stock)

# names = set()
# names.add('Martin')
# names.add('Jana')
# names.add('Petr')
# names.add('Simona')
# print(len(names), names)

# names.add('Martin')
# print(len(names), names)

# t = 1, 2, 3, 2, 3, 2, 3, 1, 2
# s = set(t)
# print(type(s), s)
# d = list(t)
# print(type(d), d)

# text = '''Prágl
# Prágl, po anglánsku Prague nebo Praha nebo v Cajsku, je taková lochna
# v tem kuse hródy někde za čárama naši domoviny, kde se zoncna už
# nechláme a kde se prndá po cajzlovsku. A ještě k temu tam majó sicnu
# těžcí papaláši, kvůli čemu ho má každé v láfu jako kaktus ve véfuku.
# Z Práglu bere kramále aj ten jejich len kerému se péruje Vltava.

# O Práglu se taky kóří, pač tam majó hafo retychů pro všecky. Kromě
# bůry švédských retychů só aj dva v Olmecu a jeden v Bučovicách.
# To my z našeho štatlu radši hážem lulec do kašny na Zelňáku. Když
# ale nekdo vopruboval zašrajbčit náš barocké Parnas do cancu retychů
# pro všecky, přišmrdolili se ti Švédi s tým, že só proti a hókajó po
# celé hródě, že ta vasra v tem se dá chlemtat.
# '''

# mySet = set(text)
# print(type(mySet))
# print(len(mySet))
# newList = tuple(mySet)
# print(sorted(newList))

# item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}

# if "weight" in item:
#     print(f"Hmotnost předmětu je {item['weight']} kg.")
# else:
#     print("Hmotnost není zadána.")

# item["weight"] = 0.95
# item["weight"] += 0.55

# if "weight" in item:
#     print(f"Hmotnost předmětu je {item['weight']} kg.")
# else:
#     print("Hmotnost není zadána.")

# Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota známka z daného předmětu. 
# Pro zjednodušení vlož do slovníku pouze tři předměty (například český jazyk, matematiku a dějepis). Vypiš obsah slovníku pomocí funkce print().

# schoolReport = {"Czech Language": 2, "Math": 1, "English": 3}
# for subject, grade in schoolReport.items():
#     print(f"For {subject} you have got {grade}")

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

# ticket = int(input("What is your ticket number?"))
# if ticket in tombola:
#     print(tombola[ticket])
# else:
#     print("Bohužel nevyhráváš nic.")

# passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

# name = input("What is your name?: ")
# if name in passwords:
#     passcode = input("What is your password?: ")
#     if passwords[name] == passcode:
#         print("Please come on in.")
#     else:
#         print("Oh no you di'in't!")
# else:
#     print("Get away from here you fraud!")


# sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}
# print(len(sausages))
# sausages.pop("CDAry")
# print(len(sausages))

# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }

# totalSales = 0
# for bookName, bookPrints in sales.items():
#     totalSales += bookPrints
#     print(f"We have sold {bookPrints} of {bookName}")
# print(f"Total book sales are {totalSales}")
# print(sum(sales.values()))

# books = [
#     {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
#     {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
#     {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
# ]

# overAllMoney = 0
# totalSales = 0
# for item in books:
#     overAllMoney = overAllMoney + item["sold"] * item["price"]
#     totalSales += item["sold"]
# print(overAllMoney)
# print(totalSales)

# sales2019 = 0
# for item in books:
#     if item["year"] == 2019:
#         sales2019 += item["sold"]
# print(sales2019)

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

# average = sum(school_report.values()) / len(school_report)
# print(average)

# for subject, mark in school_report.items():
#     if mark == 1:
#         print(subject)

# books = [
#     {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
#     {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
#     {"title": "Past", "pages": 390, "rating": 4},
#     {"title": "Popel popelu", "pages": 411, "rating": 10},
#     {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
#     {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
#     {"title": "Zločinný steh", "pages": 542, "rating": 8},
#     {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
#     {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
# ]

# allPagesRead = 0
# for item in books:
#     allPagesRead += item["pages"]

# print(allPagesRead)

# ratingMoreEqualEight = 0
# namesRatingMoreEqualEight = []
# fullInfoRatingMoreEqualEight = []

# for item in books:
#     if item["rating"] >= 8:
#         ratingMoreEqualEight += 1
#         namesRatingMoreEqualEight.append(item["title"])
#         fullInfoRatingMoreEqualEight.append(item)

# print(ratingMoreEqualEight)
# print(namesRatingMoreEqualEight)
# print(fullInfoRatingMoreEqualEight)



# Napiš program, který vypíše všechny majitele, jejichž vozidlo je registrováno v Plzeňském kraji, tj. na druhém místě (index 1!) řetězce v klíči je písmeno P.

# plates = {"4A2 3000": "František Novák",
#     "6P5 4747": "Jana Pilná",
#     "3B7 3652": "Jaroslav Sečkár",
#     "1P5 5269": "Marta Nováková",
#     "37E 1252": "Martina Matušková",
#     "2A5 2241": "Jan Král"}

# pilsen = 0
# for plateName, carOwner in plates.items():
#     if plateName[1].lower() == "p":
#         pilsen += 1

# print(pilsen)


# Uložte si tuto strukturu do proměnné recept na začátek nového programu. Vypište pomocí funkce print kolik bude celé jídlo stát korun zaokrouhlené na celé koruny nahoru.
# recipe = {
#     'nazev': 'Batáty se šalvějí a pancettou',
#     'narocnost': 'stredni',
#     'doba': 30,
#     'ingredience': [
#         ['batát', '1', '15 kč'],
#         ['olivový olej', '2 lžíce', '2 kč'],
#         ['pancetta', '4-6 plátků', '21 kč'],
#         ['přepuštěné máslo', '2 lžíce', '5 kč'],
#         ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
#         ['sůl', '1/2 lžičky', '0.1 kč'],
#         ['muškátový oříšek', 'špetka', '1 kč'],
#         ['česnek', '2 stroužky', '1 kč'],
#         ['šalvějové lístky', '20-25', '12 kč']
#     ]
# }
# prices = []

# for money in recipe["ingredience"]:
#     costOfFood = float(money[2].split(" ")[0])
#     prices.append(costOfFood)

# totalPrice = math.ceil(sum(prices))

# print(totalPrice)


purchase_list = [
    {"Jméno": "Petr", "Položka": "Prací prášek", "Částka": 399},
    {"Jméno": "Ondra", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Petr", "Položka": "Toaletní papír", "Částka": 65},
    {"Jméno": "Libor", "Položka": "Pivo", "Částka": 124},
    {"Jméno": "Petr", "Položka": "Pytel na odpadky", "Částka": 75},
    {"Jméno": "Míša", "Položka": "Utěrky na nádobí", "Částka": 130},
    {"Jméno": "Ondra", "Položka": "Toaletní papír", "Částka": 120},
    {"Jméno": "Míša", "Položka": "Pečící papír", "Částka": 30},
    {"Jméno": "Zuzka", "Položka": "Savo", "Částka": 80},
    {"Jméno": "Pavla", "Položka": "Máslo", "Částka": 50},
    {"Jméno": "Ondra", "Položka": "Káva", "Částka": 300}
]

eachPersonCosts = {}

for person in purchase_list:
    name = person["Jméno"]
    money = person["Částka"]
    if name in eachPersonCosts:
        eachPersonCosts[person["Jméno"]] += money
    else:
        eachPersonCosts[name] = money

print(eachPersonCosts)