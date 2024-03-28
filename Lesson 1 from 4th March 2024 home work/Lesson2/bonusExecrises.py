import random
#TASK 1
# def fillOutSpacesFromLeft(number, spaceLimit):
#     number = str(number)
#     for cycle in range(spaceLimit+1):
#         lengthOfNumber = len(number)
#         if lengthOfNumber < spaceLimit:
#             number = "." + number
#     return number



# listOfNumbers = [7728, 88, 958621, 5941, 959847272, 3944, 80, 521, 57035, 3967894]
# maxLength = 0
# for value in listOfNumbers:
#     if len(str(value)) > maxLength:
#         maxLength = len(str(value))


# print(maxLength)
# for item in listOfNumbers:
#     print(fillOutSpacesFromLeft(item, maxLength))




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




#TASK 3
# Slovo je stále možné pohodlně přečíst, když jsou pomíchaná písmena. 
# Stačí, když první a poslední písmeno je na své pozici zachováno. 
# Napiš funkci, která bude mít jako vstupní parametr slovo a vrátí slovo, kde zpřehází všechny znaky kromě prvního a posledního.

# Nápověda: random.shuffle()

# Super bonus: Napiš program, který takovou funkci využije na delší text více slov.

def shuffleWordExclFirstAndLastChar(wordOfChoice):
    wordAsList = list(wordOfChoice)
    middle = wordAsList[1:-1]
    random.shuffle(middle)
    newShuffledList = [wordAsList[0]] + middle + [wordAsList[-1]]
    return("".join(newShuffledList))

shuffledWord = shuffleWordExclFirstAndLastChar("lovers")
print(shuffledWord)


# def countPenalty(numberOfAxles, mass):
#     fine = 0
#     for axlesByLaw, massByLaw in requirements:
#         if numberOfAxles == axlesByLaw:
#             if mass > massByLaw:
#                 fine = (mass-massByLaw) * 1000
#     return fine

# requirements = [(5, 48), (4, 32), (3, 25), (2, 18)]

# fineToPay = countPenalty(5, 48)
# if fineToPay == 0:
#     print("There is no fine. You're all set well. Have a safe trip!")
# else:
#     print(f"The fine is {fineToPay} CZK.")






