# Uvažuj, že navrhuješ software pro zásilkovou společnost.

# Vytvoř třídu Package, která bude mít tři atributy - address, weight a state. Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.



class Package:
    def __init__(self, address, weight, state):
        # Vrať se k návrhu software pro zásilkovou společnost. U třídy Package uprav atribut state tak, aby byl chráněný. Ověř, že vytváření objektů i výpisy informací o něm fungují.
        self.address = address
        self._weight = weight
        self.state = state

    # Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. Uvažuj například větu 
    # "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".
        
    # def get_info(self):
    #     return f"Balík na adresu {self.address} má hmotnost {self.weight} je ve stavu {self.state}"
    
    # U třídy Package přejmenuj metodu get_info() na __str__() a vyzkoušej, jestli nyní stačí k získání informací o balíku funkce print().
    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self._weight} je ve stavu {self.state}"

    # Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. Cena přepravy je daná hmotností balíku. Cena přepravy balíku do 10 kg je 129 Kč, 
    # cena přepravy balíku od 10 kg do 20 kg je 159 Kč a cena přepravy balíků těžších než 20 kg je 359 Kč. 
    # Metoda spočítá cenu a vrátí ji jako číslo.

    def delivery_price(self):
        if self._weight < 10:
            return 129
        elif self._weight < 20:
            return 159
        else:
            return 359
    # Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku a zaznamená tak jeho doručení. 
    # Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen. Pokud ano, metoda vrátí zprávu "Balík již byl doručen". 
    # Tím bude řidič (řidička) informován(a) o tom, že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku. 
    # Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo".
    
    def deliver(self):
        if self.state == "doručen":
            return "Balík již byl doručen"
        else:
            self.state = "doručen"
            return "Doručení uloženo"
    
# Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. 
# U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
    
package1 = Package("Bieblova 165, Brno", 5.67, "doručen")
package2 = Package("Hochmanova 214, Louny", 11.48, "nedoručen")
package3 = Package("Strnadova 14, Chomutov", 27.13, "doručen")

# Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.

# print(book1.get_info())
# print(book2.get_info())
# print(book3.get_info())
# print(package1)
# print(package1.deliver())
# print(package1)

# Vyzkoušej metodu deliver(). Co se stane, pokud ji u jednoho balíku zavoláš dvakrát?
# print(package1.deliver())
print(package1._weight)
package1._weight -= 2
print(package1._weight)

# print(book1)
# print(book1.deliver())
# print(book1.delivery_price())
# print(book2.delivery_price())
# print(book3.delivery_price())

