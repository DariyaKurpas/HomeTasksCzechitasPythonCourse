# Modifikujte program pro počítání výplaty z předchozí sekce tak, aby nevypisoval průměrnou výplatu za rok, nýbrž aby vypsal konkrétní vyplacenou částku pro každý měsíc zvlášť.
# Nejprve tyto informace vypište na terminál
# Poté program upravte tak, aby vypsal tyto výsledky do souboru

path = r"my_excerices\vykaz.txt"
hours_yearly = []
with open(path, encoding="utf-8") as file:
    for hour_count in file:
        hours_yearly.append(int(hour_count))

print(hours_yearly)

hourly_wage = float(input("What is your hourly wage in EUR:\n"))

monthly_wage = [month * hourly_wage for month in hours_yearly]
for index, payroll in enumerate(monthly_wage, start=1):
    print(f"Month {index}: {payroll} EUR.")

with open("my_excerices\monthly_wage.txt", mode="w", encoding="utf-8") as file:
    for index, payroll in enumerate(monthly_wage, start=1):
        print(f"Month {index}: {payroll} EUR", file=file)




# # Otevření souboru a načtení hodin do seznamu
# vykaz = []
# with open('reseni-cviceni/lekce-09/01-cteni-souboru/vykaz.txt', 'r') as soubor:
#     for radek in soubor:
#         vykaz.append(int(radek.strip()))

# # Získání hodinové mzdy od uživatele
# hodinova_mzda = float(input("Zadejte vaši hodinovou mzdu: "))

# # Výpočet výplaty za každý měsíc
# výplaty = [hodiny * hodinova_mzda for hodiny in vykaz]

# # Výpis výplat za každý měsíc na terminál
# for index, vyplata in enumerate(výplaty, start=1):
#     print(f"Měsíc {index}: {vyplata} Kč")

# # Zápis výplat do souboru
# with open('vypis_vyplat.txt', 'w') as soubor:
#     for index, vyplata in enumerate(výplaty, start=1):
#         soubor.write(f"Měsíc {index}: {vyplata} Kč\n")
 
