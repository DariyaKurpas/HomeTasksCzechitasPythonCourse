import math, statistics, random
# Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
# U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. 
# V takovém případě vyberte jako střed číslo blíže ke konci seznamu.

# s = [1, 3, 4, 5, 7, 9, 10]
# middle = len(s) // 2
# if len(s) % 2 == 0:
#     middle -= 1

# print(s[middle])

# s = [1, 3, 4, 5, 7, 9]
# middle = len(s) // 2
# if len(s) % 2 == 0:
#     middle = math.ceil(middle)

# print(s[middle])

#Uložte si do proměnné jmeno svoje jméno. Pomocí volání vhodných metod jej převeďte nejdříve na malá písmena a poté na velká písmena.

# name = "DaRInka"

# print(name.lower())
# print(name.upper())

# hodnoty = ['12', '1', '7', '-11']
# hodnoty[2] = int(hodnoty[2])
# hodnoty[2] += 4
# hodnoty[2] = str(hodnoty[2])
# print(hodnoty)

# hodnoty = ['12', '1', '7', '-11']
# hodnoty[2] = str(int(hodnoty[2])+4)
# print(hodnoty)

# hodnoty = '12.1 1.68 7.45 -11.51'
# newList = hodnoty.split(" ")  - SPLIT ALWAYS CREATES A LIST OF SPLITTED PARTS OF THE APPLIED STRING
# newList[-1] = float(newList[-1])
# newList[-1] = str(newList[-1] + 0.25)
# print(" ".join(newList))

# Napište program, který dostane na vstupu desetinné číslo a na výstup napíše toto 
# číslo zaokrouhlené nejdříve nahoru, potom dolů a potom běžným Pythonovským zaokrouhlováním.

# number = 10.954
# print(math.ceil(number))
# print(math.floor(number))
# print(round(number))

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

# importantSubjects = []

# for subject in school_report:
#     if subject[0] == "Český jazyk" or subject[0] == "Anglický jazyk" or subject[0] == "Matematika" or subject[0] == "Fyzika":
#         importantSubjects.append(subject[1])
# averageOnImpSubj = statistics.mean(importantSubjects)

# print(f"The average score on important subjects is {averageOnImpSubj}.")

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


# print(f"Nejvice zamestnancu hlasovalo pro {statistics.mode(votes)}")


# s = [1, 3, 4, 5, 7, 9, 10, 5, 7, 7]
# print(statistics.mode(s))

# tempsColumns = [[2001, 7.8],
#          [2002, 8.7],
#          [2003, 8.2],
#          [2004, 7.8],
#          [2005, 7.7],
#          [2006, 8.2],
#          [2007, 9.1],
#          [2008, 8.9],
#          [2009, 8.4],
#          [2010, 7.2]
# ]

# tempsRows = [[item[0] for item in tempsColumns], [item[1] for item in tempsColumns]]

# #Získejte teplotu na třetím řádku tabulky.
# print(tempsColumns[2][1])

# # Získejte rok na pátém řádku tabulky.
# print(tempsColumns[4][0])

# #Získejte poslední řádek tabulky jako seznam.
# print(tempsColumns[-1])

# # Vytvořte tabulku bez prvních dvou řádků.
# print(tempsColumns[2:])

# # Vytvořte tabulku pouze z prvních dvou řádků.
# print(tempsColumns[:2])

# # Vytvořte tabulku obsahující jen řádky 5, 6, 7, 8 (myšleno při "lidském" číslování, tj. od 1).
# print(tempsColumns[4:8])

# # Použitím proměnné sloupce vypište seznam teplot seřazený vzestupně podle velikosti. Šlo by to i pomocí proměnné radky, ale to ještě neumíme.
# print(sorted(tempsRows[1]))

# scores = [["student a", 9, 7, 8, 5],
#           ["student b", 5, 3, 6, 6],
#           ["student c", 8, 4, 9, 7],
#           ["student d", 8, 5, 4, 8],
#           ["student e", 10, 6, 10, 7]
#           ]

# points = [(36, 1), (32, 2), (26, 3), (20, 4), (0, 5)]

# for studentResults in scores:
#     totalScore = sum(studentResults[1:])
#     for totalPoint, mark in points:
#         if totalScore > totalPoint:
#             print(f"{studentResults[0]} has received {mark}.")
#             break

# averages = []
# for i in range(1, 5):
#     average = sum(student[i] for student in scores) / len(scores)
#     averages.append(average)

# print(averages)

# questionOne = [score[1] for score in scores]
# questionTwo = [score[2] for score in scores]
# questionThree = [score[3] for score in scores]
# questionFour = [score[4] for score in scores]

# averages = [(sum(questionOne) / len(questionOne)), (sum(questionTwo) / len(questionTwo))]

# print(min(averages))

# averageQuestionOne = sum(questionOne) / len(questionOne)
# averageQuestionTwo = sum(questionTwo) / len(questionTwo)
# print(averageQuestionOne)
# print(averageQuestionTwo)
        
# questionScores = []
# for cycle in range(1, 5):
#     tempList = []
#     for score in scores:
#         tempList.append(score[cycle])
#     questionScores.append(tempList)

# print(questionScores)

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

# pohovor = sum("pohovor" in oneAkce for oneAkce in akce)
# jazyky = []
# for oneAkce in akce:
#     # if "pohovor" in oneAkce:
#     #     pohovor += 1
#     if "jazykový kurz" in oneAkce:
#         jazyky.append(oneAkce)
# print(pohovor)
# print(jazyky)

# uniqueJazyky = []
# for lang in jazyky:
#     parts = lang.split(" - ")
#     if parts[1] not in uniqueJazyky:
#         uniqueJazyky.append(parts[1])
# # print(uniqueJazyky)

# Stříbrná medaile je sice úžasný úspěch, ale kdo by nechtěl vyhrát? Podívejme se, kolik chybělo stříbrnému běžci k vítězství.

# Nejprve si vytvoř dvě proměnné, do kterých ulož čas vítěze a čas závodníka se stříbrnou medailí. Oba časy převeď na minuty a ulož jako číslo.
# Vypočti rozdíl obou proměnných. Tím zjistíš, kolik minut chybělo stříbrnému závodníku k vítězství.

# vysledky = [
#     ["Brunner Radek", [3, 0, 9]], 
#     ["Urban Jaroslav", [3, 11, 44]], 
#     ["Andrle Jakub", [3, 12, 21]], 
#     ["Fiala Stanislav", [3, 13, 31]]
# ]

# timeGold = float(vysledky[0][1][0] * 60 + vysledky[0][1][1] + (100*vysledky[0][1][2]/60/100))
# timeSilver = float(round(vysledky[1][1][0] * 60 + vysledky[1][1][1] + (100*vysledky[1][1][2]/60/100), 2))
# print(timeSilver, timeGold)
# difference = round(timeSilver - timeGold, 2)
# print(f"The time difference is {difference}")

# Zadání je podobné jako u předchozího příkladu, ale nyní zkusíme výpočet provést pro všechny závodníky.

# Nejprve (pomocí cyklu a metody append()) vytvoř dvourozměrný seznam, kde na nulté pozici vnořeného seznamu je číslo běžce a na první pozici je čas 
# běžce v minutách jako desetinné číslo.
# Ve druhém kroku (opět pomocí cyklu a metody append()) vytvoř další dvourozměrný seznam, 
# kde na nulté pozici vnořeného seznamu je číslo běžce a na první pozici je rozdíl času běžce oproti času vítěze v minutách. 
# Jinak řečeno, bude tam číslo, které udává, o kolik by běžec musel být rychlejší, aby závod vyhrál.

# shortSummary = []
# for cycle in range(4):
#     time = float(round(vysledky[cycle][1][0] * 60 + vysledky[cycle][1][1] + (100*vysledky[cycle][1][2]/60/100), 2))
#     tempList = [cycle, time]
#     shortSummary.append(tempList)
# print(shortSummary)

# for cycle in range(4):
#     for runner in vysledky:
#         print(runner[cycle+1][1])

# sumupDifference = [shortSummary[0]]
# for cycle in range(1, 4):
#     timeDiff = round(shortSummary[cycle][1] - shortSummary[0][1], 2)
#     difference = [cycle, timeDiff]
#     sumupDifference.append(difference)

# print(sumupDifference)
# for index, runner in enumerate(shortSummary):
#     timeDiff = shortSummary[]



# Vypište seznam čísel každé na nový řádek zarovnané vpravo na délku nejdelšího čísla.

# numbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
# Návod:

# Zjistěte kolik znaků zabírá nejdelší číslo ze seznamu
# Napište funkci, která dostane řetězec a délku, na kterou má text vyplnit zleva mezerami
# Bonus: funkce bude mít volitelný parametr, jakým znakem má text vyplňovat
# length = []
# for item in numbers:
#     ultimateLength = len(str(item))
#     length.append(ultimateLength)
# print(length) 

# for number in numbers:
#     for cycle in range(max(length)):
#         if len(str(number)) < max(length):
#             number = "." + str(number)
#     print(number)

# Napiš funkci, která bude jednoduchou simulací rulety. Budeme uvažovat pouze možnost sázení na řady. Uživatel si může vybrat jednu ze tří řad:

# první řada (hodnoty 1, 4, 7 atd.),

# druhá řada (hodnoty 2, 5, 8 atd.),

# třetí řada (hodnoty 3, 6, 9 atd.).

# Zeptej se uživatele, na kterou ze tří řad sází a na výši sázky.

# Vytvoř funkci roulette, která bude mít parametry číslo řady a výši sázky. 
# Pomocí funkce randint z modulu random vygeneruj náhodné číslo v rozsahu od 0 (včetně) do 36. Vyhodnoť, do které řady číslo náleží. 
# Nezapomeň, že 0 nepatří do žádné z řad a pokud padne, uživatel vždy prohrává.

# Funkce roulette vrací hodnotu výhry. Pokud uživatel vsadil na správnou řadu, vyhrává dvojnásobek sázky, v opačném případě nevyhrává nic jeho sázka propadá.


# allSets = [[1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
#            [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
#            [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
#            ]

# def roulette(set, bet):
#     number = random.randint(0, 36)
#     print(f"the random number is {number}")
#     if number == 0:
#         bet = 0
#         exit()

#     for index, predefinedSet in enumerate(allSets, 1):
#         if number in predefinedSet:
#             print(f"The winning set is {index}.")
#             break
#     if set == index:
#         bet *= 2
#     else:
#         bet = 0
#     return bet

# userSet = int(input("Your choice of set: "))
# userBet = int(input("Your choice of bet: "))       

# betReturn = roulette(userSet, userBet)

# if  betReturn > 0:
#     print(f"You have won! Your bet is now {betReturn}")
# elif betReturn == 0:
#     print(f"You have lost. Your bet is now {betReturn}")


#TASK 2
# def roulette(set, bet):
#     randomNumber = random.randint(0, 36)
#     for index, predefinedSet in enumerate(allSets, 1):
#         if randomNumber in predefinedSet:
#             print(f"Set {index} won.")
#     if set == predefinedSet:
#         bet *= 2
#         print(f"You have won! Your best has been doubled, it is now {bet}")
#     else:
#         bet = 0
#         print(f"You have lost. Your bet is now {bet}")
#     print(f"the random number is {randomNumber}.")

# allSets = [
#     [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34],
#     [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35],
#     [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]
# ]

# usersChoiceSet = int(input("Which set are you betting on? Choose 1, 2 or 3"))
# usersChoiceBet = int(input("How much are you betting?"))

# roulette(usersChoiceSet-1, usersChoiceBet)

# Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena. 
# Stačí, když první a poslední písmeno je na své pozici zachováno. 
# Napiš funkci, která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny znaky kromě prvního a posledního.

# Nápověda: random.shuffle()

# def wordShuffle(word):
#     if len(word) < 3:
#         return word
#     listOfLetters = list(word)
#     middle = listOfLetters[1:-1]
#     random.shuffle(middle)
#     shuffledWord = "".join([listOfLetters[0]] + middle + [listOfLetters[-1]])
#     return shuffledWord

# def wordShuffle(word):
#     if len(word) < 3:
#         return word
#     middle = list(word[1:-1])
#     random.shuffle(middle)
#     shuffledWord = word[0] + "".join(middle) + word[-1]
#     return shuffledWord

# print(wordShuffle("beautiful"))

# def textShuffle(text):
#     listOfWords = text.split(" ")
#     listOfShuffledWords = []
#     for word in listOfWords:
#         if len(word) < 3:
#             listOfShuffledWords.append(word)
#         else:
#             middle = list(word[1:-1])
#             random.shuffle(middle)
#             newWord = word[0] + "".join(middle) + word[-1]
#             listOfShuffledWords.append(newWord)
    
#     return " ".join(listOfShuffledWords)

def textShuffle(text):
    separateWords = text.split(" ")
    shuffledText = []
    for word in separateWords:
        if len(word) < 3:
            shuffledText.append(word)
        else:
            middle = list(word[1:-1])
            random.shuffle(middle)
            newWord = word[0] + "".join(middle) + word[-1]
            shuffledText.append(newWord)
    return " ".join(shuffledText)

print(textShuffle("What a beautiful day it is today"))
