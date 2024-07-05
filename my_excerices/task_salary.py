# path = r"my_excerices\mereni.txt"
# with open(path, encoding="utf-8") as file:
#     text = file.read()

# print(text)

# path = r"my_excerices\mereni.txt"
# lines = []
# with open(path, encoding="utf-8") as file:
#     for line in file:
#         lines.append(line)

# print(lines)

# path = r"my_excerices\mereni.txt"
# output = []
# with open(path, encoding="utf-8") as file:
#     for line in file:
#         day, temp = line.split("\t")
#         output.append([day, temp])

# print(output)

# path = r"my_excerices\mereni.txt"
# output = []
# with open(path, encoding="utf-8") as file:
#     for line in file:
#         day, temp = line.split("\t")
#         output.append([day, float(temp)])

# print(output)

###############################################
# Zatím jsme výplatu počítali za předpokladu, že každý měsíc odpracujeme stejný počet hodin, což není příliš realistické. Stáhněte si textový soubor vykaz.txt, který obsahuje 12 řádků a na každém řádku počet odpracovaných hodin za každý měsíc za poslední rok.

# Otevřete tento soubor ve svém programu a načtěte hodnoty na řádcích do seznamu vykaz. Vytiskněte tento seznam do terminálu funkcí print() abyste si ověřili, že jste soubor načetli správně.
# Nechte uživatele zadat na příkazovém řádku hodinovou mzdu. Spočítejte a na výstup vytiskněte celkovou výplatu za celý rok a průměrnou výplatu na jeden měsíc.

path = r"my_excerices\vykaz.txt"
hours_yearly = []
with open(path, encoding="utf-8") as file:
    for hour_count in file:
        hours_yearly.append(int(hour_count))

print(hours_yearly)

hourly_wage = float(input("What is your hourly wage in EUR:\n"))
average_monthly_wage = sum(hours_yearly) * hourly_wage / len(hours_yearly)
total_year_wage = sum(hours_yearly) * hourly_wage

print(f"Your yearly salary is {total_year_wage} EUR and on average per month it's {round(average_monthly_wage, 2)} EUR. Congrats!")

continue = https://kodim.cz/czechitas/uvod-do-progr-2/uvod-do-programovani-2/soubory/cteni-souboru/vyplata-presneji