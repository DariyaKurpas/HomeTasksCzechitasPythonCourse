# path = r'my_excerices\slohovka.txt'
# slohovka_as_list = []
# with open(path, encoding="utf-8") as file:
#     for line in file:
#         slohovka_as_list.append(line)

# words_in_slohovka = []
# for item in slohovka_as_list:
#     line = item.split()
#     words_in_slohovka.append(line)

# word_count = 0
# for item in words_in_slohovka:
#     word_count += len(item)

# print(word_count)


# path = r'my_excerices\slohovka.txt'
# slohovka_as_list = []
# with open(path, encoding="utf-8") as file:
#     slohovka_as_list = file.readlines()


# word_count = 0
# for item in slohovka_as_list:
#     line = item.split()
#     print(f"This line contains {len(line)} words.")
#     for word in line:
#         word_count += 1


# print(f"The total count of words in this document is {word_count}.")







# Otevření souboru a načtení řádků do seznamu
seznam_radku = []
with open('my_excerices\slohovka.txt', 'r', encoding='utf-8') as soubor:
    seznam_radku = soubor.readlines()

# Analýza počtu slov na řádcích a výpis
celkovy_pocet_slov = 0
print("Počet slov na řádku:")
for radek in seznam_radku:
    slova = radek.split()
    pocet_slov = len(slova)
    print(pocet_slov)
    celkovy_pocet_slov += pocet_slov

# Výpis celkového počtu slov
print(f"Celkový počet slov v dokumentu: {celkovy_pocet_slov}")
