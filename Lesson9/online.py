# import datetime as dt

from datetime import datetime, timedelta, date

print(datetime.now())
print(datetime.today())
print(date.today())

my_var = datetime(2024, 5, 1, 13, 00)
print(my_var)
print(my_var.weekday()) # 0-6
print(my_var.isoweekday()) # 1-7

# Czech Rep 1.5.2024


print(my_var.isoformat()) # adds a T between the date and time: 2024-05-01T13:00:00
print(my_var.strftime("%Y")) # year
print(my_var.strftime("%m")) # month
print(my_var.strftime("%d")) # day
print(my_var.strftime("%M")) # minute
print(my_var.strftime("%d. %m. %Y, %H:%M"))
print(my_var.strftime("%H:%M, %d. %m. %Y"))

print(my_var.strftime("%A"))

import locale
# locale.setlocale(locale.LC_TIME, 'cs_CZ.UTF-8') # iOS
print(locale.setlocale(locale.LC_TIME, 'cz.UTF-8')) # Windows?

string_iso = "2024-05-01T13:00:00"
print(datetime.fromisoformat(string_iso))

string = "1. 5. 2024, 18:38"
print(datetime.strptime(string, "%d. %m. %Y, %H:%M"))

today = datetime.today()
yesterday = today - timedelta(days=1.5)
print(today, yesterday)

birthday = datetime(1997, 2, 21)
print(datetime.today() - birthday)

value_timedelta = timedelta(days=10_000, hours=23, seconds=3)
print(value_timedelta)

# print(value_timedelta - birthday) # not working, check with chatGPT

print(value_timedelta.total_seconds())

# Nastavení času konce pauzy
konec_pauzy = datetime.now().replace(hour=19, minute=5, second=0, microsecond=0)

# Délka cvičení
delka_cviceni = timedelta(minutes=40)

# Výpočet času konce cvičení
konec_cviceni = konec_pauzy + delka_cviceni

# Výpis výsledného času
print("Všichni se uvidíme v", konec_cviceni.strftime('%H:%M'), "😉")
