# Napište program, který se po spuštění zeptá na název souboru, který má vytvořit (nebo přepsat, pokud už ten soubor existuje), 
# a pak se zeptá na řádek textu, který má do souboru zapsat.

# with open(f"my_exceices\{user_file_name}", mode="a", encoding="utf-8") as output_file:
#     print(user_text, file=output_file)

user_file_name = input("What should be the name of the file?\n")
with open(f"my_excerices\\{user_file_name}.txt", mode="w", encoding="utf-8") as output_file:
    output_file.write("")
while True:
    will_exit = input("Would you like to write in a file? Use Y/N:\n")
    print()
    if will_exit.strip().upper()[0] == "Y":
        print()
        user_text = input("What would you like to write in that file?\n")
        print()
        print("*****************************")
        with open(f"my_excerices\\{user_file_name}.txt", mode="a", encoding="utf-8") as output_file:
            output_file.write(f"{user_text}\n")
        print("DONE!")
    elif will_exit.strip().upper()[0] == "N":
        break
    else:
        print("Just please type Y or N.")

with open(f"my_excerices\\{user_file_name}.txt", mode="r", encoding="utf-8") as output_file:
    print(output_file.read())






