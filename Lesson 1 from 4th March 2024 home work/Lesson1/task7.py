# rodna_cisla = [
#     "845128/6219",
#     "801002/5021",
#     "900116/8291",
#     "790501/7894",
#     "850706/9259",
#     "891222/1824",
#     "870327/9582",
#     "810602/6883",
#     "850512/5070",
#     "790531/7081"
# ]

# rodnaCislaInt = []
#OPTION 1
# male = []
# female = []
# for item in rodna_cisla:
#     numericPart = item.split("/")[0]
#     # this is used to split a string
#     rodnaCislaInt.append(numericPart)

#     if item[2] == "0" or item[2] == "1":
#         male.append(int(numericPart))
#     else:
#         female.append(int(numericPart))
# print(f"Today, {len(female)} female visitor(s) came and {len(male)} male visitor(s).")
#Ending OPTION 1

#OPTION 2
# male = 0
# female = 0
# for item in rodna_cisla:
#     numericPart = item.split("/")[0]
#     # this is used to split a string
#     rodnaCislaInt.append(numericPart)

#     if item[2] == "0" or item[2] == "1":
#         male += 1
#     else:
#         female += 1
# print(f"Today, {female} female visitor(s) came and {male} male visitor(s).")
#END OF OPTION 2

#ANOTHER OPTION
# yearOfBirth = []
# oldestPatient = 0000
# youngestPatient = 9999

# for item in rodnaCislaInt:
#     year = "19" + item[0] + item[1]
#     yearOfBirth.append(int(year))

# for year in yearOfBirth:
#     if year > oldestPatient:
#         oldestPatient = year
#     if year < youngestPatient:
#         youngestPatient = year
# print(f"The youngest patient was born in {youngestPatient} and the oldest patient was born in {oldestPatient}.")
#END OF ANOTHER OPTION


#NEXT OPTION
# yearOfBirth = []

# for item in rodnaCislaInt:
#     year = "19" + item[0] + item[1]
#     yearOfBirth.append(year)
# yearOfBirth.sort()
# print(yearOfBirth)
# print(f"The youngest visitor was born {yearOfBirth[-1]} and the oldest was born {yearOfBirth[0]}.")
#END OF NEXT OPTION########################

#NEXT OPTION
# yearOfBirth = []

# for item in rodnaCislaInt:
#     year = "19" + item[0] + item[1]
#     yearOfBirth.append(year)
# for year in yearOfBirth:
#     youngest = max(yearOfBirth)
#     oldest = min(yearOfBirth)
# print(f"The youngest visitor was born {youngest} and the oldest was born {oldest}.")
#END OF NEXT OPTION


# Kolik přišlo mužů a kolik žen?
# Kdy se narodil nejstarší a kdy nejmladší pacient?
# tell python to write down only the first item in the list

#################################################

# Seznam rodných čísel pacientů
rodna_cisla = [
    "845128/6219",
    "801002/5021",
    "900116/8291",
    "790501/7894",
    "850706/9259",
    "891222/1824",
    "870327/9582",
    "810602/6883",
    "850512/5070",
    "790531/7081",
]

# Inicializace počítadel pro muže a ženy
pocet_muzu = 0
pocet_zen = 0

# Inicializace proměnných pro nejstaršího a nejmladšího pacienta
nejstarsi_datum = "999999"
nejmladsi_datum = "000000"

# Projdi všechna rodná čísla
for rodne_cislo in rodna_cisla:
    rok = rodne_cislo[:2]
    mesic = int(rodne_cislo[2:4])
    den = rodne_cislo[4:6]

    # Určení pohlaví a přizpůsobení měsíce
    if mesic > 50:
        pohlavi = "žena"
        pocet_zen += 1
        mesic -= 50
    else:
        pohlavi = "muž"
        pocet_muzu += 1
    
    # Kontrola, zda je měsíc jednociferný, a případné přidání nuly
    if mesic < 10:
        mesic_str = '0' + str(mesic)
    else:
        mesic_str = str(mesic)

    datum_narozeni = rok + mesic_str + den

    # Porovnání s dosavadními nejstarším a nejmladším datem
    if datum_narozeni < nejstarsi_datum:
        nejstarsi_datum = datum_narozeni
    if datum_narozeni > nejmladsi_datum:
        nejmladsi_datum = datum_narozeni

# # Uprav nejstarší a nejmladší datum na formát dd.mm.yy
# nejstarsi_datum = (
#     nejstarsi_datum[4:] + "." + nejstarsi_datum[2:4] + "." + nejstarsi_datum[:2]
# )
# nejmladsi_datum = (
#     nejmladsi_datum[4:] + "." + nejmladsi_datum[2:4] + "." + nejmladsi_datum[:2]
# )

# # Uprav nejstarší a nejmladší datum na formát dd.mm.yy
# nejstarsi_datum = f"{nejstarsi_datum[4:6]}.{nejstarsi_datum[2:4]}.{nejstarsi_datum[:2]}"
# nejmladsi_datum = f"{nejmladsi_datum[4:6]}.{nejmladsi_datum[2:4]}.{nejmladsi_datum[:2]}"

# Vypsání výsledků
print("Počet mužů:", pocet_muzu)
print("Počet žen:", pocet_zen)
print("Nejstarší pacient se narodil:", nejstarsi_datum)
print("Nejmladší pacient se narodil:", nejmladsi_datum)