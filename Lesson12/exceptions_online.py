# import sys

# age = input("What is your age?: ")
# if not age.isdigit():
#     print("Type a digit, you shalunishka")
#     exit()

# vek = int(age)

# if vek > 15:
#     print("Welcome!")
# else:
#     print("You are not old enough, dude")

while True:
    try:
        age = int(input("What is your age?: "))
        if age > 15:
            print("Welcome!")
            break
        else:
            print("You are not old enough, dude")
            break
    except ValueError:
        print("You have to type in a number!")
