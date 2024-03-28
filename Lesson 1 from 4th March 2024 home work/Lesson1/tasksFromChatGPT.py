#TASK 1
# Sum of Even Numbers:
# Write a program that calculates the sum of all even numbers from 1 to 100.
#Solution
#OPTION 1
# sum = 0
# for number in range (1, 100):
#     if number % 2 == 0:
#         sum += number
# print(sum)
#END OF OPTION 1
#OPTION 2
# sumOfEvens = 0
# for number in range (2, 101, 2):
#     sumOfEvens += number
# print(sumOfEvens)
#END OF OPTION 2

###############################################
#TASK 2
# Factorial Calculation:
# Write a function that calculates the factorial of a given number.
#Solution

# def factorial(n):
#     answer = n
#     for number in range (n-1, 0, -1):
#         answer *= number
#     return answer

# result = factorial(5)
# print(result)

#TASK 3 

# List Filtering:
# Given a list of numbers, create a new list that contains only the odd numbers from the original list.

#Solution

# numbers = [48, 33, 46, 12, 13, 17, 21, 98, 97, 42, 41, 37, 67, 62, 63]

# onlyOddNumbers = []

# for number in numbers:
#     if number % 2 == 1:
#         onlyOddNumbers.append(number)

# print(onlyOddNumbers)

#TASK 4

# Multiplication Table:
# Print the multiplication table for a given number (e.g., 7 * 1 = 7, 7 * 2 = 14, ...).
# Option 1
# def multiplication(number):
#     answer = 0
#     for item in range (1, 11):
#         answer = item * number
#         print(f"{item} multiplied by {number} is {answer}")

# multiplication(5)
# End of option 1

# Option 2
# def multiplication(number):
#     listOfAnswers = []
#     answer = 0
#     for item in range (1, 11):
#         answer = item * number
#         listOfAnswers.append(answer)
#     return listOfAnswers
        

# number = 5
# result = multiplication(number)
# for index, value in enumerate(result, 1):
#     print(f"{index} multiplied by {number} is {value}")

#End of option 2

#TASK 5

# Palindrome Check:
# Write a function that checks if a given word is a palindrome (reads the same backward as forward).
#OPTION 1
# def palindromeCheck(word):
#     standaloneLetters = []
#     reversed = ""
#     for item in word:
#         standaloneLetters.append(item)
#     for item in standaloneLetters:
#         reversed = item + reversed
#     if reversed == word:
#         print(f"Yes, {word} is a palindrome.")
#     else:
#         print(f"Nope, {word} is not a palindrome. Try again.")

# palindromeCheck("sunny")

#End of option 1

#Option 2 - SLICING
# def palindromeCheck(word):
#     reversedWord = word[::-1]
#     if reversedWord == word:
#         print(f"Yes, {word} is a palindrome.")
#     else:
#         print(f"Nope, {word} is not a palindrome. Try again.")

# palindromeCheck("sunny")
#END OF OPTION 2

#SLICING with a list
# list = ["Michael", "Angela", "Sunny", "John"]
# reversedlist = list[3:0:-1]
# print(reversedlist)
#



# TASK 6
# FizzBuzz Game:
# Write a program that prints the numbers from 1 to 100. For multiples of 3, print "Fizz" instead of the number. 
# For multiples of 5, print "Buzz." For numbers that are multiples of both 3 and 5, print "FizzBuzz."

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")

#     else:
#         print(number)



# TASK 7
# List Reversal:
# Write a program that reverses the order of elements in a list.
#OPTION 1
# list = ["Joshua", "Caroline", "Morgan", "Elijah", "Ben", "Alice"]
# reversedList = list[::-1]
# print(reversedList)
#END OPTION 1

#OPTION 2
# list = ["Joshua", "Caroline", "Morgan", "Elijah", "Ben", "Alice"]
# list.reverse()
# print(list)
#END OPTION 2

#OPTION 3
# list = ["Joshua", "Caroline", "Morgan", "Elijah", "Ben", "Alice"]
# print(list[::-1])
#END OPTION 3

#BONUS - sorting in descending way from Z to A
# list = ["Joshua", "Caroline", "Morgan", "Elijah", "Ben", "Alice"]
# reversedList = sorted(list, reverse = True)
# print(reversedList)

# sorted() Function:
# Basic Usage:

# sorted(iterable, key=None, reverse=False)
# iterable: The sequence to be sorted (e.g., a list, tuple, or string).
# key: A function to extract a comparison key from each element. If not provided, it uses the elements themselves.
# reverse: If set to True, the sequence is sorted in descending order.

# example: sorted_words = sorted(words, key=len) ; sorted_numbers = sorted(numbers, key=abs)



# TASK 8
# Largest Number:
# Write a function that finds the largest number in a given list.

# listOfNumbers = [99,456,758,14,13,879,654,51,212,45,46,27,879,852]
# listOfNumbers.sort()
# print(listOfNumbers[-1])

# listOfNumbers = [99,456,758,14,13,879,654,51,212,45,46,27,879,852]
# print(max(listOfNumbers))

# listOfNumbers = [99,456,758,14,13,879,654,51,212,45,46,27,879,852]
# maxNumber = 0
# for number in listOfNumbers:
#     if number > maxNumber:
#         maxNumber = number
# print(maxNumber)



# TASK 9
# Common Elements:
# Write a program that takes two lists and prints the common elements between them.
# list = ["Elena", "Sunny", "Johnny", "Bob", "Alice", "Maggy", "Peter", "Franciska", "July", "Caroline", "Don"]
# list2 = ["Sunny", "Filip", "Mark", "George", "Petr", "Franciska", "June", "Hope", "Alison", "Don"]

# for name in list:
#     if name in list2:
#         print(name)



# TASK 10
# Prime Numbers:
# Write a function that determines whether a given number is prime or not.


# def isPrime(number):
#     for division in range(2, number):
#         if noRemainder(number, division) is True:
#             return False
#         else:
#             continue
#     return True


# def noRemainder(number, divisor):
#     if number % divisor == 0:
#         return True
#     else:
#         return False

# listOfNumbers = [2, 16, 98, 88, 57, 60, 61, 17, 27, 13, 45, 9, 4, 6, 21, 43, 15]
# for number in listOfNumbers:
#     if isPrime(number) is True:
#         print("This number is prime")
#     else:
#         print("This number is not prime")



list = [5, 18, 15, 17, 23, 29, 25, 48, 46, 57]

def isPrime(number):
    for divisor in range(2, number):
        if hasNoRemainder(number, divisor) is True:
            return False
        else:
            continue
    return True


def hasNoRemainder(number, divisor):
    if number % divisor == 0:
        return True
    else:
        return False
    
for number in list:
    if isPrime(number) is True:
        print("this number is prime")
    else:
        print("This number is not prime") 
