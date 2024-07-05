user_file_name = input("How would you like to name your file?:\n")
while True:
    proceed = input("Do you want to edit the file?: \n")
    if proceed == "yes":
        user_text = input("What would you like to write in that file?:\n")

        with open(f"{user_file_name}", mode="a", encoding="utf-8") as output:
            print(user_text, file=output)
    else:
        break
