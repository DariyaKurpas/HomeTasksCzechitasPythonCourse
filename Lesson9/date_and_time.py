from datetime import datetime, timedelta

print(datetime.now())

just_a_date = datetime(year=2020, month=12, day=21)
another_date = datetime(1948, 7, 14, 23, 34, 17)

print(just_a_date)
print(another_date)


apollo_start = datetime(1969, 7, 16, 14, 32)
print(apollo_start)
print(datetime.weekday(apollo_start))
print(datetime.isoweekday(apollo_start))
print(datetime.isoformat(apollo_start))
print(datetime.strftime(apollo_start, "%d.%m.%Y v %H:%M"))

apollo_pristani = datetime.fromisoformat("1969-07-21T18:54:00")
print(apollo_pristani)


dalsi_apollo_pristani = datetime.strptime("21. 7. 1969, 18:54", "%d. %m. %Y, %H:%M")
print(dalsi_apollo_pristani)

apollo_journey = dalsi_apollo_pristani - apollo_start
print(apollo_journey)

print("*******************************************")

planovany_prijezd = datetime(2024, 3, 13, 19, 59)
zpozdeni = timedelta(minutes=10)
skutecny_prijezd = planovany_prijezd + zpozdeni
print(datetime.strftime(planovany_prijezd, "%H:%M"))
print(skutecny_prijezd)


# V proměnné apolloStart máme uložený datum a čas startu Apolla 11. 
# Vypiš datum na obrazovku ve formátu, na který jsou zvyklí Američané, tj. na první místo napiš měsíc, dále den a nakonec rok, jako oddělovače použij lomítka. Čas vypisovat nemusíš.

print(datetime.strftime(apollo_start, "%m/%d/%Y"))

# Satelit Solar Orbiter, který má za cíl pozorování Slunce, odstartoval 10. února 2020 v 5:03. Ulož si hodnotu startu do proměnné.

# Který den v týdnu Solar Orbiter odstartoval?
# Spočítej, kolik času od jeho startu uplynulo.

satellite_solar_orbiter_start = datetime(2020, 2, 10, 5, 3)
print(datetime.weekday(satellite_solar_orbiter_start))
print(datetime.isoweekday(satellite_solar_orbiter_start))

delta = datetime.now() - satellite_solar_orbiter_start
print(delta.days)


print("******************************************************")

# Zákazník si objednal večeři na webu dovážkové služby 13. listopadu 2020 v 19:47. 
# Víme, že převzetí objednávky restaurací v průměru trvá 8 minut a 35 sekund, příprava jídla trvá 30 minut a doprava jídla k zákazníkovi 25 minut a 30 sekund. 
# Kdy očekáváme, že jídlo dorazí zákazníkovi?

order_time = datetime(2020, 11, 13, 19, 47)
order_accept = timedelta(minutes=8, seconds=35)
food_prep = timedelta(minutes=30)
order_delivery = timedelta(minutes=25, seconds=30)

order_estimation_arrival = order_time + order_delivery + order_accept + food_prep + order_delivery
print(order_estimation_arrival)

print(datetime.isoformat(order_time))


print("*////////////////////////")

from datetime import datetime, timedelta

# Představme si, že máme následující časy začátku a konce přípravy
zacatek_pripravy = datetime.fromisoformat("2024-04-29T18:30:00")
konec_pripravy = datetime.fromisoformat("2024-04-29T19:15:00")
celkova_doba = konec_pripravy - zacatek_pripravy

print(celkova_doba)