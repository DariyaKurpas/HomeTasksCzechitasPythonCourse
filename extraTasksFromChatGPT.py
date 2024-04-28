# Task 1: Word Frequency Counter Write a program that takes a string as input and counts the frequency of each word in the string.
# Use a dictionary to store the word as the key and its count as the value.

# option 1
# stringExample = "I like learning Python. It is challenging, requires quite a bit of thinking and acquiring new skills. Nevertheless, it is a fun way to expand one's skills. So, here's to a new beginning!"
# frequencyCounterDict = {}
# listOfWords = list(stringExample.lower().split(" "))
# for word in listOfWords:
#     counter = 0
#     if word not in frequencyCounterDict:
#         counter += 1
#         frequencyCounterDict[f"{word}"] = counter
#     else:
#         counter += 1
#         frequencyCounterDict[f"{word}"] += counter

# print(frequencyCounterDict)

# option 2
# stringExample = "I like learning Python. It is challenging, requires quite a bit of thinking and acquiring new skills. Nevertheless, it is a fun way to expand one's skills. So, here's to a new beginning!"
# frequencyCounterDict = {}
# listOfWords = list(stringExample.lower().split(" "))
# for word in listOfWords:
#     frequencyCounterDict[word] = frequencyCounterDict.get(word, 0) + 1

# print(frequencyCounterDict)


# Task 2: Unique Value Extractor Given a list of integers, write a program that returns a set of all unique integers from the list.
# Then, convert this set back into a list and sort it in ascending order.

# myList = [1, 3, 4, 5, 78, 89, 24, 4, 5, 1, 3, 65, 2, 6, 7, 95]
# newSet = set(myList)
# print(newSet)


# Task 3: Tuple Pair Finder Write a function that takes a list of tuples (each tuple contains two integers) and an integer 'x'.
# The function should return all tuples where the sum of the two integers is equal to 'x'.

# def tuplePairFinder(pairs, numberToCheckAgainst):
#     listOfPairs = []
#     for number in pairs:
#         if isinstance(number, tuple) and len(number) == 2:
#             if number[0] + number[1] == numberToCheckAgainst:
#                 listOfPairs.append(number)
#     return listOfPairs

# myTuple = [(2, 6), (4, 4), (3, 5), (4, 5), (8, 2), (3, 2, 3)]

# print(tuplePairFinder(myTuple, 8))


# Task 4: Nested Dictionary Explorer Given a nested dictionary, write a program that prints all the keys at a given depth.
# For example, for the dictionary { "a" : { "b" : { "c" : 1 } } } and depth 2, the output should be "b".

# def print_keys_at_depth(d, target_depth, current_depth=0):
#     if current_depth == target_depth:
#         print(list(d.keys()))
#     else:
#         for value in d.values():
#             if isinstance(value, dict):
#                 print_keys_at_depth(value, target_depth, current_depth + 1)

# myDict = { "cake" : { "filling" : { "color" : "brown" } } }
# # print_keys_at_depth(myDict, 2)

# def printKeysAtDepth (dic, targetDepth, currentDepth=0):
#     if targetDepth == currentDepth:
#         print(list(dic.keys()))
#     else:
#         for value in dic.values():
#             if isinstance(value, dict):
#                 printKeysAtDepth(value, targetDepth, currentDepth+1)

# printKeysAtDepth(myDict, 2, 2)

# Task 5: List Comprehension Challenge Given a list of integers, use list comprehension to create a new list that contains the square of each integer in the original list.
# Then, use a for loop to print each element of the new list on a new line.

# myList = [1, 3, 5, 47]

# newSquareList = [item * item for item in myList]

# for item in newSquareList:
#     print(item)

# Sort a list of strings by the last letter: Given a list of strings, use a lambda function to sort the list in alphabetical order by the last letter of each string.

# myStrings = ["Darinka", "Filip", "Snouma", "Timmy", "Mexican"]

# alphabeticalOrderFromLastCharacter = sorted(myStrings, key = lambda lastLetter: lastLetter[-1])
# print(alphabeticalOrderFromLastCharacter)

# Filter out odd numbers: Given a list of numbers, use a lambda function with the filter() function to create a new list that contains only the even numbers from the original list.

# myList = [1, 2, 5, 4, 9, 7, 6, 4, 45, 37, 58, 79, 45, 64]

# onlyOddNumbers = list(filter(lambda x: x % 2 == 1, myList))
# print(onlyOddNumbers)

# Calculate the area of a rectangle: Write a lambda function that takes two arguments (length and width) and calculates the area of a rectangle.

# def areaRectangle (length, width):
#     # area = lambda length, width: length * width
#     # return area (length, width)
#     return (lambda length, width: length * width)(length, width)

# print(areaRectangle(5, 7))


# Create a list of functions: Write a lambda function that generates and returns a list of lambda functions.
# Each function in the list should calculate the power of its argument to the corresponding index in the list.
# For example, the function at index 0 should calculate the power of 0, the function at index 1 should calculate the power of 1, and so on.

# myFunctions = [lambda x: x**0, lambda x: x**1, lambda x: x**2, lambda x: x**3, lambda x: x**4]

# myFunctionsLoops = [lambda x: x ** index for index in range(1, 100)]
# for item in myFunctionsLoops:
#     print(item)

# def power_function(n):
#     return lambda x: x ** n

# myFunctionsLoops = [power_function(index) for index in range(1, 100)]

# Use reduce to find the product of a list:
# Given a list of numbers, use a lambda function with the reduce() function from the functools module to find the product of all numbers in the list.
# import functools


# myList = [1, 2, 3, 4, 5, 7, 87, 98]

# product = functools.reduce(lambda x, y: x*y, myList)
# print(product)

# Sort a list of strings by length: Given a list of strings, use a lambda function with the sort() or sorted() function to sort the strings by length.

# myStrings = ["Darinka", "Filip", "Snouma", "Timmy", "Bruno Mexican"]

# sortByLength = sorted(myStrings, key=lambda x: len(x))
# print(sortByLength)

# sortOnlyLength = sorted(map(lambda x: len(x), myStrings))
# print(sortOnlyLength)

# Filter out negative numbers: Given a list of numbers, use a lambda function with the filter() function to create a new list that only contains the positive numbers.

# negativeNumbers = [-1, -5, 13, -27, -84, 54, 67, 4]

# positiveNumber = list(filter(lambda number: number >= 0, negativeNumbers))
# print(positiveNumber)


# Transform a list of numbers: Given a list of numbers, use a lambda function with the map() function to create a new list where each number is squared
# (i.e., raised to the power of 2).

# myNumbers = [-1, -5, 13, -27, -84, 54, 67, 4]

# newList = list(map(lambda num: num ** 2, myNumbers))

# print(newList)


# Calculate factorial of a number: Write a lambda function to calculate the factorial of a number.
# The factorial of a number n is the product of all positive integers less than or equal to n.
# from functools import reduce


# def factorialCalc(number):
#     factor = list(range(1, number + 1))
#     factorial = reduce(lambda x, y: x* y, factor)
#     return factorial
# print(factorialCalc(7))

# def factorial(number):
#     factor = 1
#     for cycle in range (1, number+1):
#         factor *= cycle
#     return factor
# print(factorial(7))


# Create a list of lambda functions: Similar to the previous task you did, create a list of lambda functions where each function adds its index in the list to its argument.
# For example, the function at index 0 should add 0 to its argument, the function at index 1 should add 1 to its argument, and so on.


# def dynamicIndex(index):
#     return lambda x:x + index

# myList = [dynamicIndex(i) for i in range(1, 54)]
# print(myList[50](10))
