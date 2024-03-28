import random, statistics
# Write a function that takes a list of numbers and returns a new list containing only the even numbers.
# exampeList = [11, 5, 4, 6, 87, 89, 52, 40, 13, 17, 22, 44]
# oddNumberList = []
# for number in exampeList:
#     if number % 2 == 0:
#         oddNumberList.append(number)
# print(oddNumberList)

# Write a function that shuffles a list of words without changing the first and last letter of each word.

# def shuffleWordExcFirstLastLetter(word):
#     listOfLetters = list(word)
#     middle = listOfLetters[1:-1]
#     random.shuffle(middle)
#     shuffledList = [listOfLetters[0]] + middle + [listOfLetters[-1]]
#     return("".join(shuffledList))

# print(shuffleWordExcFirstLastLetter("homesick"))

# def shuffleTextExcFirstLastLetter(text):
#     listOfWords = text.split()
#     listOfShuffledWords = []
#     for word in listOfWords:
#         if len(word) > 3:
#             middle = list(word[1:-1])
#             random.shuffle(middle)
#             shuffledList = [word[0]] + middle + [word[-1]]
#             listOfShuffledWords.append("".join(shuffledList))
#         else:
#             listOfShuffledWords.append(word)
#     return listOfShuffledWords

# shuffledText = shuffleTextExcFirstLastLetter("I have got a brilliant idea!")
# for eachWord in shuffledText:
#     print(eachWord, end=" ")


# Write a function that takes a list of strings and returns a new list that contains the same strings but in reverse order.

# def reverseStringOrder(text):
#     newList = text[-1::-1]
#     return newList

# print(reverseStringOrder(["warm", "cold", "pretty", "xylophone", "apple"]))

# Write a function that takes a list of numbers and returns the number with the most digits.

# def identifyNumberWithMostDigits(listOfNumbers):
#     maxLength = 0
#     numberWithMostDigits = 0
#     for number in listOfNumbers:
#         number = str(number)
#         if len(number) > maxLength:
#             maxLength = len(number)
#             numberWithMostDigits = number
#     return maxLength, numberWithMostDigits

# print(identifyNumberWithMostDigits([12, 345, 45645, 75757575]))


# Write a function that takes a list of numbers and a number n, and returns a new list that contains only the numbers that are greater than n.

# def greaterThanN(numbers, n):
#     listGreaterThanN = []
#     for number in numbers:
#         if number > n:
#             listGreaterThanN.append(number)
#     return sorted(listGreaterThanN)

# print(greaterThanN([74, 54, 68, 12, 2, 3, 75, 84, 9], 55))


# Write a function that takes a list of strings and a string s, and returns a new list that contains only the strings that contain s.

# def listWithCertainLetter(listOfWords, commonLetter):
#     listWithCommonLetter = []
#     for word in listOfWords:
#         if commonLetter in word:
#             listWithCommonLetter.append(word)
#     return listWithCommonLetter

# print(listWithCertainLetter(["sunshine", "swim", "goodbye", "winter", "spring", "ciao", "bunny"], "s"))


# Write a function that takes a list of numbers and returns the median of the numbers.

# def countMedian(numbers):
#     return statistics.median(numbers)

# print(countMedian([4, 5, 8, 9, 10, 17, 18, 21, 23, 27]))

# Write a function that takes a list of numbers and returns a new list that contains the numbers in ascending order.

# def ascendingOrderNumbers(numbers):
#     ascendingOrderList = sorted(numbers)
#     return ascendingOrderList

# print(ascendingOrderNumbers([45, 57, 12, 3, 46, 69, 979]))

# Write a function that takes a list of strings and returns a new list that contains the strings sorted by length.

# def sortStrByLength(words):
#     listByLength = []
#     for word in words:
#         pass
        
# def funcSort(numbers):
#     while True:
#         change = False
#         for index in range(0, len(numbers)-1):
#             a = numbers[index]
#             b = numbers[index+1]
#             if a > b:
#                 numbers[index] = b
#                 numbers[index+1] = a
#                 change = True
#             else:
#                 numbers[index] = a
#                 numbers[index+1] = b
#         if change == False:
#             break
#     return numbers

# print(funcSort([12, 45, 46, 84, 10]))


# Write a function that takes a list of numbers and a number n, and returns the index of n in the list. If n is not in the list, the function should return -1.

# def ceasarCypher(word):
#     cypheredLetters = []
#     for letter in word:
#         letter = ord(letter)+3
#         if letter > 122:
#             letter -= 26
#         letter = chr(letter)
#         cypheredLetters.append(letter)
#     return("".join(cypheredLetters))
    
# print(ceasarCypher("zebra"))

# def shiftEncrypt(message, shiftCount):
#     cypheredLetters = []
#     shiftCount = shiftCount % 26
#     for letter in message:
#         letter = ord(letter)+shiftCount
#         if letter > 122:
#             letter -= 26
#         letter = chr(letter)
#         cypheredLetters.append(letter)
#     return("".join(cypheredLetters))

# print(shiftEncrypt("xylophone", 356))
# print(356%26)

# #passcode
# def shiftEncryptPasscode(message, passcode):
#     cypheredLetters = []
#     shiftCount = 0
#     for letter in passcode:
#         letter = ord(letter)
#         shiftCount += letter
#     shiftCount = shiftCount % 26
#     for letter in message:
#         letter = ord(letter)+shiftCount
#         if letter > 122:
#             letter -= 26
#         letter = chr(letter)
#         cypheredLetters.append(letter)
#     print(shiftCount)
#     return("".join(cypheredLetters))

# print(shiftEncryptPasscode("xylophone", "darling"))


# #text

# def shiftEncryptPasscodeText(text, passcode):
#     listOfWords = text.split(" ")
#     cypheredText = []
#     shiftCount = 0
#     for letter in passcode:
#         letter = ord(letter)
#         shiftCount += letter
#     shiftCount = shiftCount % 26
#     for word in listOfWords:
#         cypheredWord = []
#         for letter in word:
#             letter = ord(letter)+shiftCount
#             if letter > 122:
#                 letter -= 26
#             letter = chr(letter)
#             cypheredWord.append(letter)
#         cypheredText.append("".join(cypheredWord))
#     print(shiftCount)
#     return(" ".join(cypheredText))

# print(shiftEncryptPasscodeText("I have got a brilliant idea", "mother"))


# def makeMuffins(numberOfMuffins, specialIngredients = []):
#     print(f"Vyrábím {numberOfMuffins} muffinů.")
#     if specialIngredients:
#         print(f"Přidávám speciální ingredience: {", ".join(specialIngredients)}")
#     else:
#         print("No special ingredients.")
#     return numberOfMuffins

# pocet = makeMuffins(5, ["čokoláda", "vanilka"])
# print(f"Celkově vyrobeno: {pocet} muffinů.")

# Vyrábím 5 muffinů.
# Přidávám speciální ingredience: čokoláda, vanilka
# Celkově vyrobeno: 5 muffinů.