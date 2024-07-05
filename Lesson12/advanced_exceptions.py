# names = []

# file_path = r"C:\Users\dasha\HomeTasksCzechitasPythonCourse\Lesson12\names.txt"

# try:
#     with open(file_path, encoding="utf-8") as file:
#         for line in file:
#             names.append(line)
#     print(names)

# except FileNotFoundError as err:
#     print(f"The file path {file_path} is not valid. {err}")

# except PermissionError:
#     print(f"You are lacking right permissions to {file_path}")

# except Exception as err:
#     print(f"Error in loading. {err}")

# else:
#     print("Super! The file has been loaded.")

# finally:
#     print("Test finally.")

    # else probehne s try a s finally, ale finally jeste probehne i s except

while True:
    try:
        age = int(input("What is your age?: "))
        if age <= 0:
            raise ValueError("The age cannot be less than 1.")

        elif age > 15:
            print("Welcome!")
            break
        else:
            print("You are not old enough, dude")
            break
    except AttributeError:
        print("You have to type in a number!")