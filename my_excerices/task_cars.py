# Půjčovna aut má v každém kraji ČR jedno auto s danou SPZ. Ke konci roku chce zjistit, kolik všechna auta najezdila dohromady kilometrů. 
# V souboru auta.txt je pro každou SPZ zaznamenáno kolik dané auto ujelo kilometrů za daný rok. Hodnoty jsou v tisících kilometrů. Bohužel se v jednotlivých krajích blbě zkoordinovali a někdo používal desetinnou čárku, někdo zase tečku.

# Pozor! V souboru s daty je ještě jeden problém, který není na první pohled vidět!

# Napište program, který na výstup vypíše součet všech ujetých kilometrů. Jistě se vám bude hodit metoda řetězců jménem replace().


data_list = []
with open("my_excerices\cars.txt", "r", encoding="utf-8") as file:
    data_list = file.readlines()

all_distance = []
for line in data_list:
    one_input = line.strip().split()[1].replace(",", ".")
    all_distance.append(int(float(one_input)*1000))

print(f"The whole distance is {sum(all_distance)} km.")

# # Otevření souboru a načtení řádků
# celkovy_pocet_km = 0
# with open("my_excerices\cars.txt", 'r', encoding='utf-8') as soubor:
#     for radek in soubor:
#         # Odstranění přebytečných bílých znaků
#         radek = radek.replace(',', '.').strip()
#         kilometry = radek.split()[1]
#         celkovy_pocet_km += float(kilometry)
        
# # Výpis celkového součtu kilometrů
# print(f"Celkový počet kilometrů: {celkovy_pocet_km * 1000} km")  # Převod z tisíc kilometrů na kilometry

