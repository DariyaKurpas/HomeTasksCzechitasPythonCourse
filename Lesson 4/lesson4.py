import math
import statistics, functools
# data = [1, 2, 3, 4]

# print(type(data))

# data1 = 1, 2, 3, 4 # tuple
# print(type(data1))

# item = "TeaPot", 399, 1056, "England", "Czech Republic", "Ukraine" # tuple

# itemName, price, weightage, countryOfOrigin, countryOfSelling, transferCountry = item

# print(countryOfOrigin)
# print(price)
# print(itemName)

# names = set(["Darinka", "Filip"]) # one way to create a set - using tuple, alternatively I could use a list
# # The list ["Darinka", "Filip"] is indeed treated as a list. However, 
# # when you pass this list to the set() function, Python converts the list into a set. 
# # This means it removes any duplicate values (which doesn't matter in this case since "Darinka" and 
# # "Filip" are unique) and does not preserve the order of the elements, 
# # since sets are unordered collections.
# # names = {"Darinka", "Filip"} # another way to create a set
# names.add("Snouma")
# names.add("Mexican")
# names.add("Timmy")
# names.add("Snouma")
# print(type(names))
# print(len(names), names)

# letters = "l", "t", "p", "q", "r", "t", "l", "g"
# print(type(letters))
# lettersAsSet = set(letters)
# print(lettersAsSet)
# print(type(lettersAsSet))
# lettersAsList = list(letters)
# print(lettersAsList)
# print(type(lettersAsList))

# # Následující text převeďte na množinu unikátních znaků, 
# # zjistěte počet unikátních znaků a vypište jejich seřazený seznam.

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

# textAsSet = set(text)
# print(textAsSet)
# print(sorted(textAsSet))

# item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}

# title = item["title"]
# price = item["price"]
# print(title, price)

# if "price" in item:
#     print(item["price"])
# item["color"] = "blue"
# item["price"] = 2050
# item["herkunftsland"] = "Czech Republic"

# print(item)

# key = "herkunftsland"
# print(item[key])

# forNowEmptyDict = {}

# Vytvoř slovník, který reprezentuje vysvědčení. Klíč slovníku bude název předmětu a hodnota 
# známka z daného předmětu. Pro zjednodušení vlož do slovníku pouze tři předměty 
# (například český jazyk, matematiku a dějepis). Vypiš obsah slovníku pomocí funkce print().

# subjects = {"Czech Language": 5, "Meth": 1, "History": 2}
# print(subjects)
# print(subjects["Czech Language"])
# blablabla = "History"
# print(subjects[blablabla])

# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }

# sales["Noc, která mě zabila"] = 0
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

# userTicket = int(input("What is your ticket number? "))

# if userTicket in tombola:
#     print(f"Gratuluji! Vyhrali jste {tombola[userTicket]}")
# else:
#     print("Bohužel nevyhráváš nic.")

# Pořadatel našeho večírku se stává stále více paranoidním a nyní rozhodl, 
# že každý z hostů bude mít speciální heslo, které je platné jen pro něj. 
# Seznam hostů a jejich hesel je níže. Napiš program, který nejprve zkontroluje, zda je host na seznamu, 
# a pokud tam je, zeptá se ho na heslo a zkontroluje jeho správnost. 
# Hostu na seznamu, který zadá správné heslo, vypíše program text: "Smíš vstoupit."

# passwords = {"Jiří": "tajne-heslo", "Natálie": "jeste-tajnejsi-heslo", "Klára": "nejtajnejsi-heslo"}

# userName = input("What is your name? ")
# if userName in passwords:
#     userPassword = input("What is you password? ")
#     if userPassword == passwords[userName]:
#         print("You're most welcome to the party!")
#     else:
#         print("Are you trying to fool me?")
# else:
#     print("You have come to a wrong party.")

# sausages = {"Jirka": 2, "Naty": 1, "Adam": 4, "Lucka": 2, "Pavča": 2}
# print(len(sausages))

# sausages["Naty"] = 0
# print(len(sausages))

# sausages.pop("Naty")
# print(len(sausages))

# sales = {
#     "Zkus mě chytit": 4165,
#     "Vrah zavolá v deset": 5681,
#     "Zločinný steh": 2565,
# }

# totalSales = 0

# for bookName, soldPieces in sales.items():
#     totalSales += soldPieces
#     print(f"For {bookName}, {soldPieces} have been sold.")
# totalSalesShort = sum(sales.values())
# allNamesShort = sales.keys()
# print(f"The total of all sales is currently at {totalSales} pieces.")
# print(totalSalesShort)
# print(allNamesShort)
# print(sales.values())

# book = {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018}

# books = [
#     {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
#     {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
#     {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
# ]

# totalSales = 0
# income = 0
# income2019 = 0
# for item in books:
#     totalSales += item["sold"]
#     # oneBookIncome = item["sold"] * item["price"]
#     # income += oneBookIncome
#     income = income + item["sold"] * item["price"]
#     if item["year"] == 2019:
#         income2019 = income2019 + item["sold"] * item["price"]

# print(totalSales)
# print(income)
# print(income2019)


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

# averageMark = sum(school_report.values()) / len(school_report)
# print(averageMark)

# for subjectName, score in school_report.items():
#     if score == 1:
#         print(subjectName)

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
# booksMin8Star = 0
# for item in books:
#     allPagesRead += item ["pages"]
#     if item["rating"] >= 8:
#         booksMin8Star += 1
# print(allPagesRead)
# print(f"{booksMin8Star} have received the rating of 8 or higher")

# plates = {"4A2 3000": "František Novák",
#     "6P5 4747": "Jana Pilná",
#     "3B7 3652": "Jaroslav Sečkár",
#     "1P5 5269": "Marta Nováková",
#     "37E 1252": "Martina Matušková",
#     "2A5 2241": "Jan Král"}
# pilsen = 0

# for item in plates:
#     if item[1] == "P":
#         pilsen += 1

# print(pilsen)

recipe = {
    'nazev': 'Batáty se šalvějí a pancettou',
    'narocnost': 'stredni',
    'doba': 30,
    'ingredience': [
        ['batát', '1', '15 kč'],
        ['olivový olej', '2 lžíce', '2 kč'],
        ['pancetta', '4-6 plátků', '21 kč'],
        ['přepuštěné máslo', '2 lžíce', '5 kč'],
        ['mletý černý pepř', '1/2 lžičky', '0.5 kč'],
        ['sůl', '1/2 lžičky', '0.1 kč'],
        ['muškátový oříšek', 'špetka', '1 kč'],
        ['česnek', '2 stroužky', '1 kč'],
        ['šalvějové lístky', '20-25', '12 kč']
    ]
}

allPrices = []
for ingredience in recipe["ingredience"]:
    allPrices.append(float(ingredience[-1].split(" ")[0]))
print(allPrices)
    







# listOfPrices = []
# for ingredients in recipe["ingredience"]:
#     price = float(ingredients[2].split(" ")[0])
#     listOfPrices.append(price)
# totalCost = math.ceil(sum(listOfPrices))
# print(f"The total cost for the dish is {totalCost} CZK.")



# listOfPrices = []
# for ingredient in recipe['ingredience']:
#     prices = ingredient[-1].split(" ")
#     listOfPrices.append(float(prices[0]))

# totalPrice = math.ceil(sum(listOfPrices))
# print(f"The total price of the dish is {totalPrice} CZK")


# purchase_list = [
#     {"Jméno": "Petr", "Položka": "Prací prášek", "Částka": 399},
#     {"Jméno": "Ondra", "Položka": "Savo", "Částka": 80},
#     {"Jméno": "Petr", "Položka": "Toaletní papír", "Částka": 65},
#     {"Jméno": "Libor", "Položka": "Pivo", "Částka": 124},
#     {"Jméno": "Petr", "Položka": "Pytel na odpadky", "Částka": 75},
#     {"Jméno": "Míša", "Položka": "Utěrky na nádobí", "Částka": 130},
#     {"Jméno": "Ondra", "Položka": "Toaletní papír", "Částka": 120},
#     {"Jméno": "Míša", "Položka": "Pečící papír", "Částka": 30},
#     {"Jméno": "Zuzka", "Položka": "Savo", "Částka": 80},
#     {"Jméno": "Pavla", "Položka": "Máslo", "Částka": 50},
#     {"Jméno": "Ondra", "Položka": "Káva", "Částka": 300}
# ]

# sumPerPerson = {}

# for item in purchase_list:
#     person = item["Jméno"]
#     spent = item["Částka"]
#     if person in sumPerPerson:
#         sumPerPerson[person] += spent
#     else:
#         sumPerPerson[person] = spent

# print(sumPerPerson)

# totalValue = 0
# for person, value in sumPerPerson.items():
#     totalValue += value
#     print(f"{person} has spent in total {value}")

# print(f"The total costs for the group was {totalValue} CZK.")

# average = round(totalValue / len(sumPerPerson))

# print(f"On average the costs per person are {average} CZK")

# for person, spent in sumPerPerson.items():
#     difference = average - spent
#     if difference < 0:
#         print(f"{person} has paid {abs(difference)} more than average.")
#     else:
#         print(f"{person} owes {difference} to be paid.")

# books = [
#     {"title": "Zkus mě chytit", "sold": 4165, "price": 347, "year": 2018},
#     {"title": "Vrah zavolá v deset", "sold": 5681, "price": 299, "year": 2019},
#     {"title": "Zločinný steh", "sold": 2565, "price": 369, "year": 2019},
# ]

# books_2019 = list(filter(lambda item: item["year"] == 2019, books))
# print(books_2019)


# names = ["Dary", "Filip", "Snouma", "Timmy", "Mexican", "Bamboo"]


# newList = list(filter(lambda letters: len(letters) > 5, names))
# print(newList)

# newList2 = list(filter(lambda letterO: "o" in letterO, names))
# print(newList2)

# newList3 = list(filter(lambda chosenLetters: "a" in chosenLetters and "u" in chosenLetters, names))
# print(newList3)

# newList4 = list(filter(lambda chosenLetters: "u" in chosenLetters or "y" in chosenLetters, names))
# print(newList4)

# people = [
#     {"name": "Dary", "age": 27},
#     {"name": "Filip", "age": 15},
#     {"name": "Snouma", "age": 54},
#     {"name": "Timmy", "age": 3},
#     {"name": "Mexican", "age": 32},
#     {"name": "Bamboo", "age": 1}
# ]

#1 People with age higher than 30
# peopleOlderThan30 = []
# for item in people:
#     print(item["age"])


# ageMoreThan30 = list(filter(lambda person: person["age"] > 30, people))
# print(ageMoreThan30)

#2 People with name longer than 5 AND age higher than 30

# nameLongerThan5CharAndAgeHigherThan30 = list(filter(lambda onePerson: len(onePerson["name"]) > 3 and onePerson["age"] > 18, people))
# print(nameLongerThan5CharAndAgeHigherThan30)
                                             

#3 avg age

# allAges = list(map(lambda onePerson: onePerson["age"], people))
# print(allAges)

# allNames = list(map(lambda onePerson: onePerson["name"], people))
# print(allNames)

#4 max ageoin the dic

# maxAge = max(people, key= lambda onePerson: onePerson["age"])["age"]
# print(maxAge)

# maxAge = max(people, key=lambda onePerson: onePerson["age"])["age"]
# print(maxAge)

#5 max len of name

# maxLengthOfName = max(people, key=lambda onePerson: len(onePerson["name"]))["name"]
# print(maxLengthOfName)

# names = set(["Darinka", "Filip"])
# print(type(names))
# if "Darinka" in names:
#     print("She's here")

# bonbony = []
# print(type(bonbony))


# icecreamFlavours = ["chocolate", "vanilla", "vanilla"]
# print(icecreamFlavours)
# icecreamFlavoursUnique = set(icecreamFlavours)
# print(icecreamFlavoursUnique)

# cukrovi = {"chocolate": 16, "jam": 21, "blueberry": 12}

# doubleCukrovi = {}

# for type, value in cukrovi.items():
#     doubleCukrovi[type] = value * 2
# print(doubleCukrovi)




#Create a list of numbers and use a lambda function with the filter() function to get a new list that contains only the even numbers.

# numbers = [1, 3, 4, 5, 54, 62, 61, 34, 37, 84, 94]

# # evenNumbers = list(filter(lambda number: number % 2 == 0, numbers))
# # evenNumbers = []
# # for item in numbers:
# #     if item % 2 == 0:
# #         evenNumbers.append(item)

# print(evenNumbers)

#Create a list of strings and use a lambda function with the map() function to get a new list that contains the lengths of the strings.

# strings = ["sunshine", "sunflower", "sunset", "relaxation", "wellness", "spring", "summer", "autumn", "winter"]

# stringsLength = list(map(lambda word: len(word), strings))
# print(stringsLength)

# folks = [{"name": "Darinka", "age": 27},
#          {"name": "Filip", "age": 33},
#          {"name": "Snouma", "age": 3},
#          {"name": "Timmy", "age": 7},
#          {"name": "Mexican", "age": 14},
#          {"name": "Bamboo", "age": 97}
# ]

# maxAge = max(folks, key=lambda person: person["age"])
# print(maxAge)



# peopleOver20YearsOld = list(filter(lambda person: person["age"] > 20, folks))
# print(peopleOver20YearsOld)
# peopleOver20YearsOldOnlyNames = list(map(lambda onePerson: onePerson["name"], filter(lambda onePerson: onePerson["age"]> 20, folks)))
# print(peopleOver20YearsOldOnlyNames)

# onlyNames = list(map(lambda person: person["name"], folks))
# print(onlyNames)

# listOfTuples = [(19, 35), (21, 57), (1, 3), (4, 67), (57, 14)]

# newListOfTuples = sorted(listOfTuples, key=lambda tpl: tpl[1])
# print(newListOfTuples)
# listOfTuples.sort(key= lambda tpl: tpl[1])
# print(listOfTuples)

# numbersInSet = set([3, 5, 76, 54, 18, 97, 54, 68])
# print(numbersInSet)

# squares = set(map(lambda number: number * number, numbersInSet))
# print(squares)

# numbers = [1, 3, 4, 5, 54, 62, 61, 34, 37, 84, 94]

# product = functools.reduce(lambda x, y: x + y, numbers)
# print(product)

# letters = ["d", "a", "r", "i", "n", "k", "a"]

# # product = functools.reduce(lambda x, y: x + y, letters)
# # print(product)

# words = ["Have ", "a ", "beautiful ", "day", ",", " ", "you ", "lovely ", "person"]

# # product = functools.reduce(lambda x, y: x + y, words)
# # print(product)

# text = " ".join(words)
# print(text)