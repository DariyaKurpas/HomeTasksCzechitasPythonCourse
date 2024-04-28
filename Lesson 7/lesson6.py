# class Package:
#     def __init__(self, address, weight, state):
#         # Vrať se k návrhu software pro zásilkovou společnost. U třídy Package uprav atribut state tak, aby byl chráněný. Ověř, že vytváření objektů i výpisy informací o něm fungují.
#         self.address = address
#         self.weight = weight
#         self.state = state
    
#     def _mojeTajnaFunkce(self):
#         pass
#     # Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. Uvažuj například větu 
#     # "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".
    
#     # U třídy Package přejmenuj metodu get_info() na __str__() a vyzkoušej, jestli nyní stačí k získání informací o balíku funkce print().
#     def __str__(self):
#         return f"Balík na adresu {self.address} má hmotnost {self.weight} je ve stavu {self.state}"

#     # Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. Cena přepravy je daná hmotností balíku. Cena přepravy balíku do 10 kg je 129 Kč, 
#     # cena přepravy balíku od 10 kg do 20 kg je 159 Kč a cena přepravy balíků těžších než 20 kg je 359 Kč. 
#     # Metoda spočítá cenu a vrátí ji jako číslo.

#     def delivery_price(self):
#         if self.weight < 10:
#             return 129
#         elif self.weight < 20:
#             return 159
#         else:
#             return 359

#     # Přidej metodu deliver(). Půjde o obdobu tlačítka, které řidič nebo řidička zmáčkne při doručení balíku a zaznamená tak jeho doručení. 
#     # Metoda nejprve zkontroluje, zda balík náhodou již není ve stavu doručen. Pokud ano, metoda vrátí zprávu "Balík již byl doručen". 
#     # Tím bude řidič (řidička) informován(a) o tom, že se pravděpodobně spletl(a) a snaží se zaznamenat doručení u špatného balíku. 
#     # Pokud balík není ve stavu doručen, změň jeho stav právě na doručen a vrať zprávu "Doručení uloženo".
    
#     def deliver(self):
#         if self.state == "doručen":
#             return "Balík již byl doručen"
#         else:
#             self.state = "doručen"
#             return "Doručení uloženo"
        
#     # def deliveryPrice(self):
#     #     if self._weight < 10:
#     #         return 129
#     #     elif self._weight < 20:
#     #         return 159
#     #     else:
#     #         return 359
    
# # Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. 
# # U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.



# # Vytvoř třídu ValuablePackage, která dědí od třídy Package. ValuablePackage má navíc atribut value, ostatní atributy dědí od třídy Package.
# class ValuablePackage(Package):
#     def __init__(self, address, weight, state, value):
#         super().__init__(address, weight, state)
#         self.value = value
    
#     def __str__(self):
#         return super().__str__() + f". Hodnota baliku je {self.value}"
    
#     def deliveryPriceWithInsurance(self):
#         priceWithInsurance = super().delivery_price() + 6000 * 0.05
#         return priceWithInsurance
    

    
# package1 = ValuablePackage("Bieblova 165, Brno", 5.67, "nedoručen", 6000)
# package2 = Package("Hochmanova 214, Louny", 11.48, "nedoručen")
# package3 = Package("Strnadova 14, Chomutov", 27.13, "doručen")
 
# print(package1.delivery_price())
# print(package1)
# # print(package1.deliver())
# # print(package1)
# print(package1.deliveryPriceWithInsurance())
# # print(package2)
# # print(package2.delivery_price())


# Uprav třídu Package na datovou třídu. Třída bude mít atributy address, weight, a state. U každého z atributů vymysli a nastav vhodný datový typ. 
# Existující metody ve třídě ponech.

# Následně vyzkoušej, zda funguje vytváření balíků. A co cenné balíky, fungují pořád, i když dědí od datové třídy?

from dataclasses import dataclass

@dataclass
class Package:
    address: str
    weight: float
    state: str

    def __str__(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} je ve stavu {self.state}"

@dataclass
class ValuablePackage(Package):
    value: str

package1 = Package("brno", 546, "delivered")
print(package1)

package2 = ValuablePackage("bratislava", 13, "not delivered", 6000)
print(package2)

