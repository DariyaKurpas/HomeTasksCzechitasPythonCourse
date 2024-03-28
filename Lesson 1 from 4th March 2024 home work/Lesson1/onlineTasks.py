# tempCels = int(input("Type in a Celsius temperature: "))
# tempFahrSwitch = 9*tempCels/5+32

# print(tempFahrSwitch)
# print()

# tempFahr = int(input("Type in a Fahrenheit temprerature: "))
# tempCelsNew = int(round(5*(tempFahr - 32) / 9))

# print(tempCelsNew)

#####################################

# number_of_tickets = int(input("Kolik si přejete lístků? "))
# price_per_ticket = 187.75
# total_price = int(number_of_tickets * price_per_ticket)
# if total_price >= 500:
#     discount = 0.1
#     total_price = int(round(total_price * (1 - discount)))
#     print(f"Získáváte slevu {discount * 100} %")

# print(f"Celková cena nákupu je {total_price} Kč.")
#LESSON LEARNT: use int() instead of round() to make the outcome without .0
#LESSON LEARNT: first round the number, and then make an int() out of it, to make the result more precise
###########################


# number_of_tickets = int(input("Kolik si přejete lístků? "))
# price_per_ticket = 190
# total_price = number_of_tickets * price_per_ticket
# if total_price >= 500:
#     discount = 0.1
#     total_price = total_price * (1 - discount)
#     print(f"Získáváte slevu {discount * 100}.")
# else:
#     to_discount = total_price - 500
#     print(f"Nakupjte ještě za {abs(to_discount)} Kč a získáte slevu 10 %!")

# print(f"Celková cena nákupu je {total_price} Kč.")

#LESSON LEARNT: use abs() for an absolute number to make Python disregard the negative number

####################################################

# number_of_tickets = int(input("Kolik si přejete lístků? "))
# price_per_ticket = 190
# total_price = number_of_tickets * price_per_ticket
# if total_price >= 1500:
#     discount = 0.2
#     total_price = int(round(total_price * (1 - discount)))
#     print(f"Získáváte slevu {discount * 100} %")
# elif total_price >= 500:
#     discount = 0.1
#     total_price = int(round(total_price * (1 - discount)))
#     print(f"Získáváte slevu {discount * 100} %")
# else:
#     to_discount = total_price - 500
#     print(f"Nakupjte ještě za {abs(to_discount)} Kč a získáte slevu 10 %!")

# print(f"Celková cena nákupu je {total_price} Kč.")

#LESSON LEARNT: Python shall go from the highest value and disregard the rest of the ifs, so make sure to start with the highest value in the conditions


# flight_number = input("Zadejte číslo letu: ")
# prefix = flight_number[0] + flight_number[1]
# if prefix == "BA":
#     company = "British Airways"
# elif prefix == "LH":
#     company = "Lufthansa"
# else:
#     company = "Neznámá společnost"
# print(f"Letíte se společností {company}")


# flight_number = input("Zadejte číslo letu: ")
# if flight_number[0] == "B":
#     company = "British Airways"
# elif flight_number[0] == "L":
#     company = "Lufthansa"
# else:
#     company = "Neznámá společnost"
# print(f"Letíte se společností {company}")

#######################

# tasksForToday = ["yoga", "reading"]
# tasksCurrentlyPending = [tasksForToday, "study", "Python", "CyberSec", "sports"]
# newTask = input("What is next up for today? ")
# tasksForToday.append(newTask)
# print(len(tasksCurrentlyPending))
# for item in tasksCurrentlyPending:
#     print(item, end = " ")


# tasksForToday = ["yoga", "reading"]
# tasksCurrentlyPending = ["study", "Python", "CyberSec", "sports"]

# newTask = input("What is next up for today? ")
# tasksForToday.append(newTask)

# # Combine both lists
# combinedTasks = tasksForToday + tasksCurrentlyPending

# # Print the total number of tasks
# # print(len(combinedTasks))
# print(len(tasksForToday) + len(tasksCurrentlyPending))



# tasksForToday = ["yoga", "reading"]
# newTask = input("What is next up for today? ")
# tasksForToday.append(newTask)
# print(", ".join(tasksForToday))
#LESSON LEARNT: to write a list as a list, do a FOR loop, alternatively, use .join(name-of-the-list) and the separator in front of it

###############################

# guest_list = ["Darinka", "Filip"]
# incoming_person = input("Zadej jméno příchozího hosta: ")
# if incoming_person in guest_list:
#     print("Buď vítán(a)!")
# else:
#     print("Bohužel nejsi na seznamu.")

#Chceme-li si ověřit, zda je nějaká hodnota v seznamu, můžeme použít operátor in. Pro opačnou otázku, jestli prvek v seznamu není, použijeme not in.
    
#######################

# school_marks = [
#     ["Jiří", 1, 4, 3, 2],
#     ["Natálie", 2, 3, 4, 3],
#     ["Tereza", 1, 1, 2, 1],
# ]

# print(f"První student(ka) v seznamu je {school_marks[0][0]}.")
# print(f"Její/jeho poslední známka je {school_marks[0][-2]}.")
#LESSON LEARNT: using "-" for counting from the back


#####################################

# THE FOLLOWING REQUIRES MORE ATTENTION
# school_report = [
#     ["Český jazyk", 1],
#     ["Anglický jazyk", 1],
#     ["Matematika", 2],
#     ["Přírodopis", 2],
#     ["Dějepis", 1],
#     ["Fyzika", 2],
#     ["Hudební výchova", 5],
#     ["Výtvarná výchova", 2],
#     ["Tělesná výchova", 2],
#     ["Chemie", 4],
# ]

# sum_of_marks = 0
# for mark in school_report:
#     sum_of_marks += mark[1]
# average = sum_of_marks / len(school_report)
# print(f"Průměrná známka studenta/studentky je {average}.")
# print("The difficult subjects are:")

# for mark in school_report:
#     if mark[1] > 3:
#         print(f"{mark[0]}")

# # importantSubjects = [
# #     ["Český jazyk", 1],
# #     ["Anglický jazyk", 1],
# #     ["Matematika", 4],
# #     ["Fyzika", 5]
# # ]

# # sum_of_marks = 0
# # for mark in importantSubjects:
# #     sum_of_marks += mark[1]
# # averageMark = sum_of_marks / len(importantSubjects)
# # print(f"The average mark for important subjects is {averageMark} points.")
# markImpSubject = 0
# sumImpSubj = 0
# importantSubj = ["Český jazyk", "Anglický jazyk", "Matematika", "Fyzika"]
# for subject, mark in school_report:
#     if subject in importantSubj:
#         sumImpSubj += 1
#         markImpSubject += mark
# averageImpSubj = markImpSubject / sumImpSubj
# print(f"For important subjects the average mark is {averageImpSubj}")
###############################################

