# Task 1: Word Frequency Counter Write a program that takes a string as input and counts the frequency of each word in the string. 
# Use a dictionary to store the word as the key and its count as the value.

stringExample = "I like learning Python. It is challenging, requires quite a bit of thinking and acquiring new skills. Nevertheless, it is a fun way to expand one's skills. So, here's to a new beginning!"
frequencyCounterDict = {}
listOfWords = list(stringExample.lower().split(" "))
for word in listOfWords:
    counter = 0
    if word not in frequencyCounterDict:
        counter += 1
        frequencyCounterDict[f"{word}"] = counter
    else:
        counter += 1
        frequencyCounterDict[f"{word}"] += counter

print(frequencyCounterDict)



# Task 2: Unique Value Extractor Given a list of integers, write a program that returns a set of all unique integers from the list. 
# Then, convert this set back into a list and sort it in ascending order.

# Task 3: Tuple Pair Finder Write a function that takes a list of tuples (each tuple contains two integers) and an integer 'x'. 
# The function should return all tuples where the sum of the two integers is equal to 'x'.

# Task 4: Nested Dictionary Explorer Given a nested dictionary, write a program that prints all the keys at a given depth. 
# For example, for the dictionary { "a" : { "b" : { "c" : 1 } } } and depth 2, the output should be "b".

# Task 5: List Comprehension Challenge Given a list of integers, use list comprehension to create a new list that contains the square of each integer in the original list. 
# Then, use a for loop to print each element of the new list on a new line.