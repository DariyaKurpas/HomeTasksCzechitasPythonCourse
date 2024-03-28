# Napiš funkci mult, která bude mít dva číselné parametry. Funkce oba parametry vynásobí a vrátí výsledek.

# def mult(a, b):
#     return a * b

# print(mult(3, 7))

# Napište dvě funkce: kilometry_na_mile(kilometry) a mily_na_kilometry(mile), které provedou převod mezi kilometry a mílemi.

# def kmToMiles(km):
#     return km * 0.621371

# print(kmToMiles(16))

# def milesToKm(miles):
#     return miles * 1.60934

# print(milesToKm(7))

# Napište funkce: metry_na_stopy(metry) a stopy_na_metry(stopy), které umožňují převod mezi metry a stopami.

# def metresToFeet(meters):
#     return meters * 3.28084
# print(metresToFeet(35)) 

# def feetToMeters(feet):
#     return feet * 0.3048

# print(feetToMeters(30))

# Napiš funkci, která jako parametr převezme řetězec a vytiskne jej obalen hvězdičkami.

# Zadej slovo: ahoj
# ********
# * ahoj *
# ********

# def wordDeco(word, decorationSign):
#     print((len(word)+2)*decorationSign)
#     print(f"{decorationSign}{word}{decorationSign}")
#     print((len(word)+2)*decorationSign)

# wordFromUser = input("Type in a word: ")
# wordDeco(wordFromUser, "*")




# Napiš funkci month_of_birth, která bude mít jeden parametr - rodné číslo. Funkce ze zadaného rodného čísla určí měsíc narození, které vrátí jako výstup. 
# Nezapomeň, že pro ženy je k měsíci připočtena hodnota 50.

# Příklad: Pro hodnotu 9207054439 vrátí 7. Pro hodnotu 9555125899 vrátí 5.

def monthOfBirth(birthNumberNoSlash):
    birthNumberNoSlashStr = str(birthNumberNoSlash)
    month = int(birthNumberNoSlashStr[2:4])
    if month > 50:
        month -= 50
    return month

print(monthOfBirth(976221))