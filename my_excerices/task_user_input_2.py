while True:
    user_file_name = input("What should be the name of the file?\n")
    with open(f"my_excerices\\{user_file_name}.txt", mode="w", encoding="utf-8") as output_file:
        print("", file=output_file)
    while True:
        will_exit = input("Would you like to write in a file? Use Y/N:\n")
        print()
        if will_exit.strip().upper()[0] == "Y":
            print()
            user_text = input("What would you like to write in that file?\n")
            print()
            print("*****************************")
            with open(f"my_excerices\\{user_file_name}.txt", mode="a", encoding="utf-8") as output_file:
                print(user_text, end=" *** ", file=output_file)
            print("DONE!")
        elif will_exit.strip().upper()[0] == "N":
            break
        else:
            print("Just please type Y or N.")
    whole_loop_exit = input("Would you like to create a new file or completely leave?\n")
    if whole_loop_exit == "create":
        continue
    else:
        break

with open(f"my_excerices\\{user_file_name}.txt", "r", encoding="utf-8") as file:
    print(file.read(10))