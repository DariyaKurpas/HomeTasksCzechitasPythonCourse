# Task 1: Word Frequency Counter Write a program that takes a string as input and counts the frequency of each word in the string. 
# Use a dictionary to store the word as the key and its count as the value.

#option 1
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

#option 2
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

myDict = { "cake" : { "filling" : { "color" : "brown" } } }
# print_keys_at_depth(myDict, 2)

def printKeysAtDepth (dic, targetDepth, currentDepth=0):
    if targetDepth == currentDepth:
        print(list(dic.keys()))
    else:
        for value in dic.values():
            if isinstance(value, dict):
                printKeysAtDepth(value, targetDepth, currentDepth+1)

printKeysAtDepth(myDict, 2, 2)

# Task 5: List Comprehension Challenge Given a list of integers, use list comprehension to create a new list that contains the square of each integer in the original list. 
# Then, use a for loop to print each element of the new list on a new line.