# Task 10
# Prime Numbers:
# Write a function that determines 
# whether a given number is prime or not.

# Task 1: Factorial Function
# Write a Python function that calculates the factorial of a given number. 
# Test the function with various inputs.

# def factorialCalc(number):
#     factorial = 1
#     for multiplicator in range (2, number):
#         factorial *= multiplicator
#     return factorial

# factorial = factorialCalc(7)
# print(factorial)

# pocitat Fibonacci posloupnost

# a = 0
# b = 1
# for cycle in range (1, 21):
#     c = a+b
#     print(c)
#     a = b
#     b = c

# Bubble sort
# input = [2, 6, 3, 8, 97, 23, 65, 22, 0, -1]

# def sort(numbers):
#     for cycle in range(len(numbers)-1):
#         for index in range(0, len(numbers)-1):
#             a = numbers[index]
#             b = numbers[index + 1]
#             if a < b:
#                 numbers[index] = a
#                 numbers[index + 1] = b
#             else:
#                 numbers[index] = b
#                 numbers[index + 1] = a


# sort(input)
# print(input)

input = [2, 6, 3, 8, 97, 23, 65, 22, 0, -1]

def sort(numbers):
    while True:
        change = False
        for index in range(0, len(numbers)-1):
            a = numbers[index]
            b = numbers[index + 1]
            if a > b:
                numbers[index] = b
                numbers[index + 1] = a
                change = True
            else:
                numbers[index] = a
                numbers[index + 1] = b
        if change == False:
            break

sort(input)
print(input)


# caeser cypher
# def encrypt(text, passcode):
#     cypheredWord = ""
#     cypheredLetter = ""
#     for letter in text:
#         cypheredLetter = ord(letter) + 3
#         if cypheredLetter > 122:
#             cypheredLetter = ord(letter) + 3 - (122-96)
#         cypheredWord += chr(cypheredLetter)

#     return cypheredWord

# def encrypt(text, passcode):
#     cypheredWord = ""
#     cypheredLetter = ""
#     passcodeMove = 0
#     for letter in passcode:
#         letter = ord(letter)
#         passcodeMove += letter
#     for letter in text:
#         cypheredLetter = ord(letter) + passcodeMove
#         if cypheredLetter > 122:
#             cypheredLetter = (cypheredLetter - 97) % 26 + 97
#         cypheredWord += chr(cypheredLetter)
#     return cypheredWord


# caesarCypher = encrypt("zebra", "passcode")
# print(caesarCypher)


# def decrypt(text, passcode):
#     passcodeMove = 0
#     decypheredWord = ""
#     decypheredLetter = ""
#     for letter in passcodeMove:
#         letter = ord(letter)
#         passcodeMove += letter
#     for letter in text:
#         letter = ord(letter) - passcodeMove
#         if letter < 0:
#             decypheredLetter = (decypheredLetter + 97) % 26 - 97
#         decypheredWord += decypheredLetter
#     return decypheredWord

# decypher = decrypt("rwtjs", "passcode")

# def cryptogram(text, passcode):
#     decypheredWord = ""
#     decypheredLetter = ""
#     for letter in text:
#         decypheredLetter = ord(letter)-3
#         if decypheredLetter < 97:
#             decypheredLetter += 26
#         decypheredWord += chr(decypheredLetter)
#     return decypheredWord

# decypher = cryptogram("cheud")
# print(decypher)


# def cryptogram(text):


# print(ord("a"))
# print(chr(97))

# def encrypt(text)

# def decrypt(cryptogram)

# cryptogram = encrypt("zebra", "password")
# cryptogram = dencrypt("...", "password")
