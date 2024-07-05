# Vytvoř program, který vypíše výsledek dělení těchto čísel. Program se postupně zeptá na dvě čísla (mohou být celá i desetinná). 
# Vyděl tato čísla mezi sebou a vypiš výsledek dělení. Ošetři, aby program nezhavaroval při pokusu o dělení nulou. 
# V tomto případě nemusíš ošetřovat zadání nečíselného vstupu, ošetření více výjimek v jednom bloku si ukážeme v další části.

def division_two_numbers(number1, number2):
    try:
        division = number1 / number2
        if number1 != 0 or number2 != 0:
            return division
    except ValueError:
        return "One of the numbers is a zero. Please try again and avoid zero."

while True:
    number1 = float(input("Type in the first number: "))
    number2 = float(input("Type in the second number: "))
    print(division_two_numbers(number1, number2))
