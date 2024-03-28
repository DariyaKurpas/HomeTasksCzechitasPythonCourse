print("Ukol 1")
cislo = 100
print(cislo)

cislo += 1

print(cislo)
print()
print()
print()









print("""@@@@@@@@@@@@@@
Ukol 2""")

cislo = int(input("Napis sem cislo: "))
# Ulož do proměnné cislo vstup od uživatele
# cislo =

print(cislo)  # Zopakuje zadanou hodnotu
cislo += 1


print(cislo)  # Vypíše cislo zvětšené o 1
print()
print()
print()

print("""@@@@@@@@@@@@@@@@@
Ukol 3""")

userInputC = int(input("Zadej stupni Celsia: "))
celsiusNew = 9*userInputC/5+32
print(f"Podle F je teplota {celsiusNew}")

userInputF = int(input("Zadej teplotu Fahrenheit: "))
fahrenheitNew = 5*(userInputF-32)/9

print(f"Podle C je teplota {fahrenheitNew}")