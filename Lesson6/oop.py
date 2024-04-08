# employee1 = ["Darinka", "unemployed", 27]
# employee2 = ["Filip", "software engineer", 33]

# def holiday_request(days):
#     if days > employee1["holiday_entitlement"]:
#         employee1["holiday_entitlement"] = employee1["holiday_entitlement"] - days
#         print("Dovolená schválena.")
#     else:
#         print("Na tolik dní už nemáš nárok.")

# Uvažuj, že navrhuješ software pro zásilkovou společnost.

# Vytvoř třídu Package, která bude mít tři atributy - address, weight a state. Vytvoř metodu __init__, která uloží hodnoty parametrů metody do atributů.

class Package:
    def __init__(self, address, weight, state):
        self.address = address
        self.weight = weight
        self.state = state

    # Přidej metodu get_info(), která vrátí informace o balíku jako řetězec. Uvažuj například větu 
    # "Balík na adresu Václavské Náměstí 12, Praha má hmotnost 0.25 kg je ve stavu nedoručen".
    def get_info(self):
        return f"Balík na adresu {self.address} má hmotnost {self.weight} je ve stavu {self.state}"
    
    # Vytvoř metodu delivery_price(), která vypočítá cenu přepravy balíku. Cena přepravy je daná hmotností balíku. Cena přepravy balíku do 10 kg je 129 Kč, 
    # cena přepravy balíku od 10 kg do 20 kg je 159 Kč a cena přepravy balíků těžších než 20 kg je 359 Kč. 
    # Metoda spočítá cenu a vrátí ji jako číslo.

    def delivery_price(self):
        if self.weight < 10:
            return 129
        elif self.weight < 20:
            return 159
        else:
            return 359
    
# Zkus si vytvořit alespoň dva objekty ze třídy Balik. U address uvažujeme typ řetězec (str), u weight desetinné číslo. 
# U atributu state zadávej pro zjednodušení pouze dva stavy: doručen a nedoručen.
    
book1 = Package("Bieblova 165, Brno", 5.67, "doručen")
book2 = Package("Hochmanova 214, Louny", 11.48, "nedoručen")
book3 = Package("Strnadova 14, Chomutov", 27.13, "doručen")

# Vypiš informace, které generuje metoda get_info(), na obrazovku, a ověř, že je vše v pořádku.

print(book1.get_info())
print(book2.get_info())
print(book3.get_info())
print(book1.delivery_price())
print(book2.delivery_price())
print(book3.delivery_price())

# Zkus pro nakladatelství vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Book, která reprezentuje knihu. 
# Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.

class Book:
    def __init__(self, title, pages, price):
        self.title = title
        self.pages = pages
        self.price = price
    # Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.
    def get_info(self):
        return f"The book {self.title} with {self.pages} pages costs {self.price} CZK."
    
    # Přidej metodu get_time_to_read(). Metoda vrátí čas potřebný na přečtení knihy v hodinách. S využitím atributu pages vypočítej čas na přečtení knihy. 
    # Metoda bude mít nepovinný parametr, který udává počet minut potřebných pro přečtení jedné stránky knihy. 
    # Dobu potřebnou na přečtení knihy získáš jako násobek doby potřebné na přečtení jedné stránky knihy a počet stránek knihy. Výchozí hodnota nepovinného parametru je 4.
    def get_time_to_read(self, time_per_page = 4):
        time_per_book_in_hrs = self.pages * time_per_page / 60
        return time_per_book_in_hrs
    
reading1 = Book("War and Peace", 1100, 567)
reading2 = Book("The Catcher in the Rye", 327, 399)
reading3 = Book("The History of America", 976, 1100)

print(reading1.get_info())
print(reading2.get_time_to_read())
print(reading2.get_time_to_read(1))

