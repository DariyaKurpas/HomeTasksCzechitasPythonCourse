# list = [790531, 456789, 321654]

# print("scenario 1:")
# print(list)

# print("scenario 2:")
# print(list[0])

# print("scenario 3:")
# for item in list:
#     print(item)

# print("scenario 4:")
# for item in list:
#     item = str(item)
#     print(item[0])
# print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
# list2 = ["Filip", "Dary", "Klara", "Gabca"]
# print("scenario 1:")
# print(list2)

# print("scenario 2:")
# print(list2[0])

# print("scenario 3:")
# for item in list2:
#     print(item)

# print("scenario 4:")
# for item in list2:
#     print(item[0])


##LEASSON LEARNT: In Python, when you have a list of integers, you can't access individual digits directly using square brackets. 
#To work with individual digits, you need to convert each integer to a string first.
    
##LEASSON LEARNT:
# To determine whether the program will show the whole value from the list or a letter/digit from the value, you need to consider the data type of the elements in the list. 
# In your case, the elements are integers. When you print the whole list (print(list)), you see the entire integers. 
# When you access an individual element by index (print(list[0])), you get the specific integer at that position. 
# If you iterate over the list (for item in list), you are iterating over each entire integer.

# To work with individual digits or characters, you need to convert the integers to strings first.
    

# In Scenario 4, when you iterate over the strings in list2 using for item in list2: print(item[0]), you are accessing the first character of each string. Unlike Scenario 2, where you directly access the entire string with list2[0], the loop in Scenario 4 iterates over each string in the list (item) and prints only the first character (item[0]) in each iteration.

# Let me explain further:

# In Scenario 2 (print(list2[0])), you specifically access the entire string at index 0 of the list, which is "Filip".
# In Scenario 4 (for item in list2: print(item[0])), you iterate over each string in the list (item) and print only the first character (item[0]) in each iteration. 
# This results in printing the first letter of each name.
# If you want to print the entire string in Scenario 4, you should print item, not just item[0]:

# print("Scenario 4:")
# for item in list2:
#     print(item)

# This way, you will see the entire string in each iteration, similar to what you did in Scenario 3.


############################################

# flavors = ["chocolate", "vanilla", "strawberry"]
# for item in flavors:
#     if len(item) > 7:
#         print(item)

# number = float(input("Please enter a number: "))
# print(type(number))

# age = input("How old are you? ")
# print("You will be " + str(int(age) + 1) + " years old next year.")

# flavor = "chocolate"
# topping = "nuts"
# if flavor == "chocolate":
#     if topping == "nuts":
#         print("Chocolate cupcake with nuts.")

cupcakes = [["vanilla", "chocolate"], ["strawberry", "lemon"]]
print(cupcakes[0][1])