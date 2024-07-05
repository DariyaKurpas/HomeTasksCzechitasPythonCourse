from datetime import datetime, timedelta
import pytz

print(datetime.now())
print(datetime(2020, 11, 21, 20, 26, 26, 472567))

apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start)
print(datetime.weekday(apollo_start))
print(datetime.isoweekday(apollo_start))
print(datetime.isoformat(apollo_start))
print(apollo_start.strftime("%Y-%m-%d at %H:%M"))


apollo_pristani = datetime.fromisoformat("1969-07-21T18:54:00")

apollo_pristani1 = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")

just_time = datetime.strptime("2021.02.21 on Monday at 07:41", "%Y.%m.%d on Monday at %H:%M")

print(just_time.isoformat())

delka_mise = apollo_pristani - apollo_start
print(delka_mise)

planovany_prijezd = datetime(2024, 3, 13, 19, 59)
zpozdeni = timedelta(minutes=10)
skutecny_prijezd = planovany_prijezd + zpozdeni

print(skutecny_prijezd)

# V proměnné apolloStart máme uložený datum a čas startu Apolla 11. 
# Vypiš datum na obrazovku ve formátu, na který jsou zvyklí Američané, tj. na první místo napiš měsíc, dále den a nakonec rok, jako oddělovače použij lomítka. Čas vypisovat nemusíš.

us_apollo_start = apollo_start.strftime("%m-%d-%Y")
print(us_apollo_start)

# Satelit Solar Orbiter, který má za cíl pozorování Slunce, odstartoval 10. února 2020 v 5:03. Ulož si hodnotu startu do proměnné.

# Který den v týdnu Solar Orbiter odstartoval?
# Spočítej, kolik času od jeho startu uplynulo.

satellite_start = datetime(2020, 2, 10, 5, 3)
print(datetime.isoweekday(satellite_start))
delta = datetime.today() - satellite_start
print(delta)

print(datetime.today())

print(datetime.now(pytz.timezone("US/Eastern")))

# Zákazník si objednal večeři na webu dovážkové služby 13. listopadu 2020 v 19:47. Víme, že převzetí objednávky restaurací v průměru trvá 8 minut a 35 sekund, 
# příprava jídla trvá 30 minut a doprava jídla k zákazníkovi 25 minut a 30 sekund. Kdy očekáváme, že jídlo dorazí zákazníkovi?

order_placed = datetime(2020, 11, 13, 19, 47)
accept_order = timedelta(minutes=8, seconds=35)
prep_food = timedelta(minutes=30)
delivery_food = timedelta(minutes=25, seconds=30)
arrival_food = order_placed + accept_order + prep_food + delivery_food
print(arrival_food)