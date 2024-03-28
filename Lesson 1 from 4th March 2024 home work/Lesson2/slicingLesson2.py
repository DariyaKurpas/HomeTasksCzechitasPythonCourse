import math, statistics
# SLICING

# venecky = [1, 2, 4, 1, 6, 0, 1, 45, 67]
# venecky[0] = 3
# print(venecky)
# print(venecky[0:5])
# print(venecky[:5])
# print(venecky[5:])
# print(venecky[3::2])
# print(venecky[:5] + venecky[5::2])

# string = "Mate radsi more nebo hory?"
# print(len(venecky))
# print(sum(venecky))
# print(min(venecky))
# print(max(venecky))
# print(sorted(venecky))

# print(len(string))
# print(sum(string)) - nefunguje
# print(min(string)) # podle abecedy
# print(max(string))
# print(sorted(string, reverse=True))

# ad = "You shall be using Python on the job."

# if "Python" in ad: # check with Filip why for loop is not working here!
#     print("Beru to!")

# if "Python" not in ad:
#     print("Neberu to!")


# pohyby = [1200, -250, -800, 540, 721, -613, -222]

# print(pohyby[2])
# print(pohyby[2:])
# print(len(pohyby))
# print(min(pohyby))
# print(max(pohyby))
# print(sum(pohyby))

# Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. 
# Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém seznamu. Otestujte jej na seznamech různých délek.

# s = [1200, -250, -800, 540, 721, -613, -222]

# average = sum(s) / len(s)
# print(round(average, 2))
# print(int(round(average)))





# difference = max(s) - min(s)
# print(difference)


###################################


#HOMEWORK

# goodies = [2, 6, 10, 8, 0, 5, 7]
# print(goodies[2])
# goodies[3] += 5 # or goodies[3] = 13
# print(goodies[3])
# print(goodies[2:5])
# print(goodies[:5])
# print(goodies[3:])

# print(len(goodies))
# print(sum(goodies))
# print(min(goodies))
# print(max(goodies))
# print(sorted(goodies))

# goodies = ['apple', 'cherry', 'banana']
# print(sorted(goodies))  # Output: ['apple', 'banana', 'cherry']
# print(goodies)  # Output: ['apple', 'cherry', 'banana']

# name = "dariya" + " " + "kurpas"
# print(name[2:12])
# print(name[2])
# print(name[:5])
# print(len(name))

# ad = "we are looking for an active person with a great deal of creativity"
# if "creativity" in ad:
#     print("I love it!")
# if "Python" not in ad:
#     print("neeeeehhhh")

# listOfNames = ["dariya", "filip", "snouma", "timmy", "bruno"]

#task 1

# pohyby = [1200, -250, -800, 540, 721, -613, -222]
# # Vypište v pořadí třetí pohyb z uvedeného seznamu.
# print(pohyby[2])
# # Vypište všechny pohyby kromě prvních dvou.
# print(pohyby[2:])
# # Vypište kolik je všech pohybů dohromady.
# print(len(pohyby))
# # Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
# print(max(pohyby))
# print(min(pohyby))
# # Spočítejte celkový přírůstek na účtu za dané období. Pozor, že přírůstek může vyjít i záporný.
# print(sum(pohyby))

# s = [1, 5, 8, 46, 45, 78, 15, 13, 40]

# print(sum(s) / len(s))

# average = sum(s) / len(s)
# print(average)
# print(round(average))
# print(int(round(average)))
# print(int(average))

# # Postupujte obdobně jako v úložce Průměr, ale tentokrát sestavte výraz pro výpočet rozpětí, tedy rozdílu mezi minimální a maximální hodnotou.
# s = [1, 5, 8, 46, 45, 78, 15, 13, 40]
# print(max(s) - min(s))

# rozpeti = max(s) - min(s)
# print(rozpeti)

# Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
# U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. V takovém případě vyberte jako střed číslo blíže ke konci seznamu.
# list with odd number of values
# s = [1, 5, 8, 46, 45, 78, 15, 13, 64]
# if len(s) % 2 == 0:
#     middle = len(s) / 2 -1
# # elif len(s) % 2 == 1:
# #     middle = len(s) // 2
# elif len(s) % 2 == 1:
#     middle = math.ceil(len(s)/2)

# print(s[middle])

# middle = int(len(s) / 2)
# print(s[middle])

# s = [1, 5, 8, 46, 45, 78, 15, 13, 64, 17]
# print(s[int(len(s)/2)])

# s = [1, 5, 8, 46, 45, 78, 15, 13, 64, 17]
# middle = int(len(s) / 2)
# print(s[middle])

# s = [1, 5, 8, 46, 45, 78, 15, 13, 64]
# middle = len(s) // 2
# if len(s) % 2 == 0:
#     middle -= 1
# print(s[middle])

# print("dariya".upper())
# name = "dariya"
# print(name.upper())

# print("DARINKA".lower())
# name = "DARINKA"
# print(name.lower())

# name = "           DaRINKa              "
# print(name.strip())

# ad = "do you know how to do your homework?"
# print(ad.split(sep=" "))

# ad = "do you know how to do your homework?"
# print(ad.split(" "))

# ad = "do you know how to do your homework?"
# print(ad.split(maxsplit=3))

# stringNumbers = "1.12, 4.54, 6.58"
# print(stringNumbers.split(" "))

# stringNumbers = "1.12, 4.54, 6.58"
# newList = stringNumbers.split(", ")
# print(newList)
# print("...".join(newList))

# ad = "do you know how to do your homework?"
# newText = ad.replace("you", "I")
# print(newText)

# ad = "do you know how to do your homework?"
# newText = ad.replace("your", "my").replace("you", "I").replace("do", "create")
# print(newText)

# text = "Kurz vede lektor Marek"
# novy_text = text.replace("Marek", "Martin")
# print(novy_text)

# Uložte si do proměnné jmeno svoje jméno. Pomocí volání vhodných metod jej převeďte nejdříve na malá písmena a poté na velká písmena.

# name = "DaRInka"

# print(name.upper())
# print(name.lower())

# hodnoty = ['12', '1', '7', '-11']
# hodnoty[2] = int(hodnoty[2])
# hodnoty[2] += 4
# hodnoty[2] = str(hodnoty[2])
# print(hodnoty)

# hodnoty = ['12', '1', '7', '-11']
# hodnoty[2] = str(int(hodnoty[2])+4)
# print(hodnoty)

# hodnoty = '12.1 1.68 7.45 -11.51'
# newList = hodnoty.split(" ")
# newList[-1] = float(newList[-1])
# newList[-1] += 0.25
# newList[-1] = str(newList[-1])
# print("   ".join(newList))

# hodnoty = '12.1 1.68 7.45 -11.51'
# newList = hodnoty.split(" ")
# newList[-1] = str(float(newList[-1])+0.25)
# print("   ".join(newList))

# print(math.ceil(3.1))
# print(math.floor(7.7))
# print(round(4.25, 1))
# print(round(4.25))

# average = statistics.mean([12, 45, 46, 74, 1, 12, 13, 2])
# print(average)

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

# importantSubj = []

# for subject in school_report:
#     if subject[0] == "Český jazyk" or subject[0] == "Anglický jazyk" or subject[0] == "Matematika" or subject[0] == "Fyzika":
#         importantSubj.append(subject[1])

# print(statistics.mean(importantSubj))
# print(f"The best score is {min(importantSubj)}")
# print(f"The worst score is {max(importantSubj)}")

# votes = [
#     "curling", 
#     "vánoční svařák na trzích", 
#     "vánoční svařák na trzích", 
#     "curling", 
#     "zážitková první pomoc",
#     "curling", 
#     "zážitková první pomoc",
#     "curling",
#     "zážitková první pomoc",
#     ]

# print(statistics.mode(votes))

# listOfNumbers = [1, 2, 3, 1, 2, 1, 5, 4, 5, 9]

# print(f"The most common number is {statistics.mode(listOfNumbers)}")

# rows = [
#     [2001, 7.8],
#     [2002, 8.7],
#     [2003, 8.2],
#     [2004, 7.8],
#     [2005, 7.7],
#     [2006, 8.2],
#     [2007, 9.1],
#     [2008, 8.9],
#     [2009, 8.4],
#     [2010, 7.2],
# ]

# columns = []
# columns = [[row[0] for row in rows], [row[1] for row in rows]]
# # columns = [[], []]
# # for row in rows:
# #     columns[0].append(row[0])

# # for row in rows:
# #     columns[1].append(row[1])

# # Získejte teplotu na třetím řádku tabulky.
# print(rows[2][1])
# print(columns[1][2])

# # Získejte rok na pátém řádku tabulky.
# print(rows[4][0])
# print(columns[0][4])

# # Získejte poslední řádek tabulky jako seznam.
# print(rows[-1])

# # Vytvořte tabulku bez prvních dvou řádků.
# for item in rows[2:]:
#     print(item)

# # Vytvořte tabulku pouze z prvních dvou řádků.

# print(rows[:2])

# for item in rows[:2]:
#     print(item)


# # Vytvořte tabulku obsahující jen řádky 5, 6, 7, 8 (myšleno při "lidském" číslování, tj. od 1).

# for item in rows[4:8]:
#     print(item)

# # Použitím proměnné sloupce vypište seznam teplot seřazený vzestupně podle velikosti. Šlo by to i pomocí proměnné radky, ale to ještě neumíme.
# sortedColumnsList = sorted(columns[1]) # print(sorted(columns[1])) wouldn't have had modified the list as well, only .sort() would have
# print(sortedColumnsList)

# studentsScores = [
#     ["Student A", 9, 7, 8, 5],
#     ["Student B", 5, 3, 6, 6],
#     ["Student C", 8, 4, 9, 7],
#     ["Student D", 8, 5, 4, 8],
#     ["Student E", 10, 6, 10, 7]
# ]

# points = [(36, 1), (32, 2), (26, 3), (20, 4), (0, 5)]
# for studentX in studentsScores:
#     totalScore = sum(studentX[1:])
#     for score, point in points:
#         if totalScore >= score:
#             print(f"{studentX[0]} has received {point} points")
            # break


# for studentX in studentsScores:
#     totalScore = sum(studentX[1:5])
#     if totalScore >= 36:
#         print(f"{studentX[0]} has received point 1")
#     elif totalScore >= 32:
#         print(f"{studentX[0]} has received point 2")
#     elif totalScore >= 26:
#         print(f"{studentX[0]} has received point 3")
#     elif totalScore >= 20:
#         print(f"{studentX[0]} has received point 4")
#     else:
#         print(f"{studentX[0]} has received point 5")



studentsScores = [
    ["Student A", 9, 7, 8, 5],
    ["Student B", 5, 3, 6, 6],
    ["Student C", 8, 4, 9, 7],
    ["Student D", 8, 5, 4, 8],
    ["Student E", 10, 6, 10, 7]
]

# grades = [(36, 1), (32, 2), (26, 3), (20, 4), (0, 5)]

# for studentX in studentsScores:
#     totalScoreOfStudent = sum(studentX[1:])
#     for score, grade in grades:
#         if totalScoreOfStudent >= score:
#             print(f"{studentX[0]} has received {grade}")
#             break

# questionA = [studentX[1] for studentX in studentsScores]
# questionB = [studentX[2] for studentX in studentsScores]
# questionC = [studentX[3] for studentX in studentsScores]
# questionD = [studentX[4] for studentX in studentsScores]

# averageOnQuestions = [statistics.mean(questionA), statistics.mean(questionB), statistics.mean(questionC), statistics.mean(questionD)]

# for index, questions in enumerate(averageOnQuestions, 1):
#     print(f"For question {index} the average is {questions}")

# averageOnQuestions = []

# for i in range (1, 5):
#     averageQs = sum(student[i] for student in studentsScores) / len(studentsScores)
#     averageOnQuestions.append(averageQs)

# for numberOfQuestion, score in enumerate(averageOnQuestions, 1):
#     print(f"For question {numberOfQuestion} the score is {score}")


# akce = [
#     "školení - řízení firemních vozidel",
#     "jazykový kurz - angličtina",
#     "pohovor - Jan Dvořák",
#     "pohovor - Antonín Sova",
#     "jazykový kurz - němčina",
#     "pohovor - Iveta Hájková",
#     "pohovor - Ivan Brož",
#     "pohovor - Katarína Martináková",
#     "setkání se zákazníkem - Metrostav",
#     "jazykový kurz - angličtina",
#     "školení - vykazování práce",
#     "pohovor - Klaudie Moudrusová",
# ]

# sumOfPohovor = sum("pohovor" in item for item in akce)
# print(sumOfPohovor)


# countOfPohovor = 0
# for eachString in akce:
#     if "pohovor" in eachString:
#         countOfPohovor += 1
# print(f"Uskutecnilo se {countOfPohovor} pohovoru")

# jazykoveKurzy = []

# for eachString in akce:
#     if "jazykový kurz" in eachString:
#         if eachString not in jazykoveKurzy:
#             jazykoveKurzy.append(eachString)
# for item in jazykoveKurzy:
#     print(f"The employees are interested in {item}")

# languages = []
# for entry in akce:
#     if "jazykový kurz" in entry:
#             languages.append(entry.split(" - ")[1])
# print(languages)

# uniques = []
# for language in languages:
#       if language not in uniques:
#             uniques.append(language)
# print(uniques)

# print("The highest interest is in:")
# for item in languages:
#     print(item)
    



# names = ["Dariya", "Snouma", "Filip", "Snouma", "Timmy", "Bruno", "Snouma"]

# sumOfSnoumas = sum("Snouma" in name for name in names)
# print(sumOfSnoumas)