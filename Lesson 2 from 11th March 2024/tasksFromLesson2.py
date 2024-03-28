import statistics, math
#TASK 1

# pohyby = [1200, -250, -800, 540, 721, -613, -222]
# Vypište v pořadí třetí pohyb z uvedeného seznamu.
# Vypište všechny pohyby kromě prvních dvou.
# Vypište kolik je všech pohybů dohromady.
# Pomocí volání vhodných funkcí vypište nejvyšší a nejnižší pohyb.
# Spočítejte celkový přírůstek na účtu za dané období. 
# Pozor, že přírůstek může vyjít i záporný.

# print(pohyby[2])
# print(pohyby[2:])
# print(len(pohyby))
# print(min(pohyby))
# print(max(pohyby))
# print(sum(pohyby))

#TASK 2

# Mějme proměnnou s, ve které předpokládáme uložený nějaký seznam. 
# Sestavte v výraz (vzoreček), který spočítá průměrnou hodnotu v takovém seznamu. 
# Otestujte jej na seznamech různých délek.
s = [7, 13, 21, 54, 71, 3]
# average = sum(s) / len(s)
# print(average)

# Postupujte obdobně jako v úložce Průměr, 
# ale tentokrát sestavte výraz pro výpočet rozpětí, tedy rozdílu mezi minimální a maximální hodnotou.

# difference = max(s) - min(s)
# print(difference)

# Sestavte výraz, který vrátí číslo nacházející se přesně uprostřed v zadaném seznamu s. 
# U seznamů liché délky je střed jasně definovaný, ovšem u seznamů sudé délky nám padne mezi dvě čísla. 
# V takovém případě vyberte jako střed číslo blíže ke konci seznamu.

# index = len(s)//2
# # if len(s) % 2 == 1:
# #     index = math.ceil(index)
# if len(s) % 2 == 0:
#     index -= 1
# print(s[int(index)])

# index = len(s)/2
# if len(s) % 2 == 1:
#     index = math.floor(index)
# elif len(s) % 2 == 0:
#     index -= 1
# print(s[int(index)])

# limitationsByLaw = [(5, 48), (4, 32), (3, 25), (2, 18)]

# def countPenalty (numberOfAxis, mass):
#     penalty = 0
#     for limitsAxis, limitWeightage in limitationsByLaw:
#         if numberOfAxis == limitsAxis:
#             if mass > limitWeightage:
#                 penalty = (mass - limitWeightage) * 1000
#     return penalty

# print(countPenalty(2, 32))

# control = [
#     [4, 33],
#     [2, 19],
#     [3, 29],
#     [3, 27],
#     [5, 53],
#     [5, 51],
#     [2, 20],
# ]
# totalPenalty = 0
# for index, eachVehicle in enumerate(control, 1):
#     penalty = countPenalty(eachVehicle[0], eachVehicle[1])
#     print(f"The penalty for vehicle {index} is {penalty} CZK")
#     totalPenalty += penalty

# print(f"The total penalty is {totalPenalty} CZK")