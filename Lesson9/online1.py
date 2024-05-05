from datetime import datetime, timedelta

# V proměnné apolloStart máme uložený datum a čas startu Apolla 11. 
# Vypiš datum na obrazovku ve formátu, na který jsou zvyklí Američané, tj. na první místo napiš měsíc, dále den a nakonec rok, jako oddělovače použij lomítka. Čas vypisovat nemusíš.

apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start)

apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start.strftime("%m-%d-%Y %H:%M"))
print(apollo_start.strftime("%m/%d/%Y %H:%M"))
print(apollo_start.strftime("%m-%d-%Y"))

# Satelit Solar Orbiter, který má za cíl pozorování Slunce, odstartoval 10. února 2020 v 5:03. Ulož si hodnotu startu do proměnné.

# Který den v týdnu Solar Orbiter odstartoval?
# Spočítej, kolik času od jeho startu uplynulo.

start_satellite_solar_orbiter = datetime(2020, 2, 10, 5, 3)
launch_day = datetime.strftime("%A") # why not working???
print(datetime.weekday(start_satellite_solar_orbiter))
print(datetime.isoweekday(start_satellite_solar_orbiter))

print(datetime.now() - start_satellite_solar_orbiter)

print(f"Solar Orbiter has launched on {launch_day}")


# Zákazník si objednal večeři na webu dovážkové služby 13. listopadu 2020 v 19:47. Víme, že převzetí objednávky restaurací v průměru trvá 8 minut a 35 sekund, 
# příprava jídla trvá 30 minut a doprava jídla k zákazníkovi 25 minut a 30 sekund. Kdy očekáváme, že jídlo dorazí zákazníkovi?

order_timestamp = datetime(2020, 11, 13, 19, 47)
order_process_time = timedelta(minutes=8, seconds=35)
prep_time = timedelta(minutes=30)
delivery_time = timedelta(minutes=25, seconds=30)

arrival_time = order_timestamp + order_process_time + prep_time + delivery_time
print(arrival_time)

string = "13. 1. 2023, 15:45"

regular_timestamp = datetime.strptime(string, "%d. %m. %Y, %H:%M")

print(regular_timestamp.strftime("%m-%d-%Y %H:%M"))