# def mult(a, b):
#     return a * b

# def calcMileToKm(miles):
#     return miles * 1.60934

# def calcKmToMile(km):
#     return km * 0.621371

# def calcFootToMeter(foot):
#     return foot * 0.3048

# def calcMeterToFoot(meter):
#     return meter * 3.28084

# def calcCmToInch(cm):
#     return cm * 0.393701

# def calcInchToCm(inch):
#     return inch * 2.54

# def calcKgToLbs(kg):
#     return kg * 2.20462

# def calcLbsToKg(lbs):
#     return lbs * 0.453592

# def calcLitreToGallon(litre):
#     return litre * 0.264172

# def calcGallonToLitre(gallon):
#     return gallon * 3.78541

# def calcCelsiusToFahrenheit(celsius):
#     return 9*celsius/5+32

# def calcFahrenheitToCelsius(fahrenheit):
#     return 5*(fahrenheit-32)/9


# Napiš funkci total_price, která vypočte cenu noci v hotelu. 
# Funkce bude mít dva parametry - persons a breakfast. Cena za noc za osobu je 850 Kč a cena za snídani za osobu je 125 Kč. 
# Funkce vrátí výslednou cenu. Parametr breakfast je nepovinný a výchozí hodnota je False.

# Funkci vyzkoušej se zadáním dvou i jedné hodnoty, např. total_price(3), total_price(2, True).

# def priceForHotelStay(numberOfPersons: int, hadBreakfast=False) -> int:
#     pricePerNight = 850
#     breakfastPrice = 125
#     if hadBreakfast:
#         return (numberOfPersons * pricePerNight) + (numberOfPersons * breakfastPrice)
#     else:
#         return numberOfPersons * pricePerNight

# print(f"The total price for the stay in our hotel is {priceForHotelStay(3, True)}")

# def salaryCalc (workingDays: float, overtime: float = 0) -> float:
#     hourlyRate = 215
#     workingDayComp = hourlyRate * 8 * workingDays
#     overtimeCompensation = overtime * (hourlyRate * 1.25)
#     return workingDayComp + overtimeCompensation

# print(salaryCalc(21.4))

# muffins = "čokoládový, vanilkový, borůvkový"

# print(muffins.split(", ")[1])
# print(", ".join(['čokoláda', 'vanilka']))

# Jak byste vytvořili seznam, který obsahuje čísla od 1 do 5 použitím funkce range()?
# numbers = []
# for i in range(1, 5):
#     numbers.append(i)

# print(numbers)

# numbersAutom = list(range(1 , 6))
# print(numbersAutom)

# Import statistics Library
# import statistics

# # # Calculate middle values
# print(statistics.median([1, 3, 5, 7, 9, 11, 13]))
# print(statistics.median([1, 3, 5, 7, 9, 11, 13, 15, 17, 19]))
# print(statistics.median([-11, 5.5, -3.4, 7.1, -9, 22]))

# def pekarna(muffin, cukroví=None):
#     print(f"you have got a {muffin} with {cukroví}")

# pekarna("cokolada")

# def pridej_cukr(mnozstvi, jednotka="lžičky"):
#     return f"{mnozstvi} {jednotka} cukru"

# print(pridej_cukr(3))

# def vyrob_muffiny(pocet_muffinu, specialni_ingredience = []):
#     print(f"Vyrábím {pocet_muffinu} muffinů.")
#     if specialni_ingredience:
#         print(f"Přidávám speciální ingredience: {', '. join(specialni_ingredience)}")
#     else:
#         print("Bez speciálních ingrediencí")
#     return pocet_muffinu

# pocet = vyrob_muffiny(5, ["čokoláda", "vanilka"])
# print(f"Celkově vyrobeno: {pocet} muffinů.")

# vyrob_muffiny(5, ["čokoláda", "vanilka"])

