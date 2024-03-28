numbers = [1, 99, 456, 54, 78, 3, 45, 68, 99, 74, 65, 17, 13, 44, 22]

numbersOdd = []
numbersEven = []
for number in numbers:
    if number % 2 == 1:
        numbersOdd.append(number)
    else:
        numbersEven.append(number)
numbersOdd.sort()
numbersEven.sort()
print("The odd numbers are:", numbersOdd)
print("The even numbers are:", numbersEven)
# for num in numbersOdd:
#     print(num, end = ", ")
    
# print()
# print()

# numbersEven = []
# # for number in numbers:
# #     if number % 2 == 0:
# #         numbersEven.append(number)
# # print("The even numbers are:")
# # for num in numbersEven:
# #     print(num, end = " ")

# # join() works only with strings! if I wanted to use it, I'd need to first convert the list into string.
# for number in numbers:
#     if number % 2 == 0:
#         number = str(number)
#         numbersEven.append(number)
# print("The even numbers are:")
# print(", ".join(numbersEven))