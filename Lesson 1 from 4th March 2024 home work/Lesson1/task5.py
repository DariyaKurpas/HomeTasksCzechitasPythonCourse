numbers = [1, 99, 456, 54, 78, 3, 45, 68, 99, 74, 65, 17, 13, 44, 22, 3, 45, 99, 5, 68, 44, 44, 78]
print("The initial list contains", len(numbers), "numbers of elements.")
numbersNoDuplicates = []
for num in numbers:
    if num not in numbersNoDuplicates:
        numbersNoDuplicates.append(num)

print("This is the list without duplicates:")
for num in numbersNoDuplicates:
    print(num, end = ", ")
print()
print()
print("The new list contains", len(numbersNoDuplicates), "numbers of elements.")




# for num in numbers:
#     if num not in numbersNoDuplicates:
#         #i cannot convert NUM now into a string, because it will not longer be recogized as a number and won't be checked for duplicates in the list.
#         numbersNoDuplicates.append(num)


# print("This is the list without duplicates:", ", ".join(numbersNoDuplicates))

#possible workarounds:
# converting a list into strings: 

# original_list = [1, 2, 3, 4, 5]
# string_list = [str(element) for element in original_list]
# print(string_list)

# Keep in mind that this creates a new list, and the elements of the original list remain unchanged. If you want to modify the original list in place, you can use a loop to iterate over the indices of the list and update each element:

# original_list = [1, 2, 3, 4, 5]
# for i in range(len(original_list)):
#     original_list[i] = str(original_list[i])
# print(original_list)

