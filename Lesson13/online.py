import re

regex_rodne_cislo = re.compile(r"\d{9,10}")
# print(regex_rodne_cislo)

text = "My birth number is 9516487595"
fullmatch = "9516487595"
begin_match = "9516487595 is my birthnumber"

# print(regex_rodne_cislo.fullmatch(text))
# print(regex_rodne_cislo.fullmatch(fullmatch))
# print(regex_rodne_cislo.fullmatch(begin_match))

if regex_rodne_cislo.fullmatch("012345678"):
    print("ok")
else:
    print("not OK")

if regex_rodne_cislo.fullmatch(fullmatch):
    print("ok")
else:
    print("not OK")

if regex_rodne_cislo.fullmatch(text):
    print("ok")
else:
    print("not OK")

if regex_rodne_cislo.fullmatch(".12345678"):
    print("ok")
else:
    print("not OK")

some_text = """
Zápisy o provedených vyšetřeních:
Pacient 6407156800 trpěl bolestí zad a byl poslán na vyšetření. 
Pacientka 8655057477 přišla na kontrolu po zranění kotníku.
Do ordinace telefonovala pacientka 7752126712, které byl elektronicky vydán recept na Paralen. 
"""

print(regex_rodne_cislo.findall(some_text))

print(regex_rodne_cislo.sub("---this is not your business---", some_text))
print(regex_rodne_cislo.sub("X" * 10, some_text))