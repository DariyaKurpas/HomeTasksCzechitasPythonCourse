# Uvažuj, že navrhuješ software pro zásilkovou společnost.
# Vytvoř třídu Package, která bude mít tři atributy - address, weight a state. Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.

class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self._state = state
    # Přidej metodu get_info(), která vrátí informace o balíku jako řetězec.
    # Uvažuj například větu "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".

    # def getInfo(self):
    #     return f"Balík na adresu {self.address} má hmotnost {self.weight} je ve stavu {self.state}"

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} je ve stavu {self._state}"

    # Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. Cena přepravy je daná hmotností balíku.
    # Cena přepravy balíku do 10 kg je 129 Kč, cena přepravy balíku od 10 kg do 20 kg je 159 Kč a cena přepravy balíků těžších než 20 kg je 359 Kč.
    # Metoda spočítá cenu a vrátí ji jako číslo.
    def deliveryPrice(self):
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359

    # Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku a zaznamená tak jeho doručení.
    # Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen. Pokud ano, metoda vrátí zprávu "Balík již byl doručen".
    # Tím bude řidič (řidička) informován(a) o tom, že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku.
    # Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo".

    def delivery(self):
        if self._state == "doručen":
            return "Balík již byl doručen"
        else:
            self._state = "doručen"
            return "Doručení uloženo"


# Zkus si vytvořit alespoň dva objekty ze třídy Balik.
# U address uvažujeme typ řetězec (str), u weight desetinné číslo. U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
balik1 = Package("Mrkosova 35, Brno", 22.456, "nedoručen")
balik2 = Package("Jugoslavska 35, Brno", 7.12, "nedoručen")
balik3 = Package("Namesti SNP 12, Brno", 45.54, "dorucen")

# print(balik1)
# print(balik2)
# print(balik3)

# print(f"You have to pay {balik1.deliveryPrice()} for the package")
# print(f"You have to pay {balik2.deliveryPrice()} for the package")
# print(f"You have to pay {balik3.deliveryPrice()} for the package")

print(balik1.delivery())
print(balik1)
print(balik1.delivery())

# Přepravní společnost musí rozdělovat balíky do jednotlivých aut.
# Při plánování dopravy je potřeba hlídat, zda pro jeden automobil není naplánována přeprava příliš velkého množství balíků.
# Vytvoř tedy tři objekty třídy Package.  Dále vytvoř seznam package_list, do kterého vlož vytvořené objekty. Příklad objektů a seznamu je níže.

packageList = [balik1, balik2, balik3]

# Vytvoř si proměnnou total_weight, do které si s využitím cyklu budeš ukládat celkovou hmotnost všech balíků. Na začátku bude mít hodnotu 0.

totalWeight = 0
invoiceForEShop = 0

for package in packageList:
    totalWeight += package.weight
    invoiceForEShop += package.deliveryPrice()

print(totalWeight)
print(invoiceForEShop)
