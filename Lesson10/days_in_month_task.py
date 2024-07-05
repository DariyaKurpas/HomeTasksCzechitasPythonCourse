pocty_dni = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

with open("calendar.txt", mode="w", encoding="utf-8") as output:
    for item in pocty_dni:
        print(item, file=output)