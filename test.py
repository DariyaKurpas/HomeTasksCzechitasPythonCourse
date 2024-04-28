# print("two types of quotes. This one \" and this one\'")





# Třída Item: jedná se o základní třídu pro všechny položky, které lze objednat. Atribut "name" reprezentuje název položky; řetězec. Atribut "price" reprezentuje cenu položky; float.
# Metoda __str__() vrací řetězcovou reprezentaci položky ve formátu: "<název>: <cena> Kč."
# Třída Item: jedná se o základní třídu pro všechny položky, které lze objednat. Atribut "name" reprezentuje název položky; řetězec. Atribut "price" reprezentuje cenu položky; float.
# Metoda __str__() vrací řetězcovou reprezentaci položky ve formátu: "<název>: <cena> Kč."
class Item:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f"{self.name}: {self.price} Kč."
    
class Pizza(Item):
    def __init__(self, name: str, price: float, ingredients: dict): # "ingredients" je slovník, kde klíče jsou názvy ingrediencí a hodnoty jejich množství v gramech
        super().__init__(name, price)
        self.ingredients = ingredients
    
    def add_extra(self, ingredient: str, quantity: int, price_per_ingredient: int):
        self.price += price_per_ingredient
        return f"Extra {ingredient}: {quantity} grams."

    def __str__(self):
        return f"Pizza {self.name}, celková cena je {self.price}" # Napište metodu __str__ tak, aby zahrnovala seznam ingrediencí a celkovou cenu.
    
class Drink(Item):
    def __init__(self, name: str, price: float, volume: int):
        super().__init__(name, price)
        self.volume = volume
    
    def __str__(self):
        return f"{self.name} v objemu {self.volume} ml stojí {self.price} Kč."
    
class Order:
    def __init__(self, name: str, address: str, items: list, status: str = "Nová"):
        self.name = name
        self.address = address
        self.items = items
        self.status = status
    
    def mark_delivered(self):
        self.status = "Doručeno."
    
    def __str__(self):
        return f"Děkujeme za objednávku! \nJméno zákazníka: {self.name} \nAdresa: {self.address} \nPoložky v objednávce: {self.items} \nStav objednávky: {self.status}"
    
class DeliveryPerson:
    def __init__(self, name: str, phone_number: str, available: bool = True, current_order: Order = ""):
        self.name = name
        self.phone_number = phone_number
        self.available = available
        self.current_order = current_order
    
    def assign_order(self, order):
        if self.available:
            Order.status = "Na cestě"
            self.available = False
        else:
            return f"Doručovatel {self.name} momentálně není volný."
        # Implementujte metodu assign_order, která přiřadí objednávku doručovateli, pokud je dostupný. 
        # Stav objednávky by měl být aktualizován na "Na cestě".

    def complete_delivery(self):
        Order.status = "Doručeno."
        self.available = True
        # Implementujte metodu complete_delivery, která označí objednávku jako doručenou a doručovatele znovu učiní dostupným pro nové objednávky.
    
    def __str__(self):
        # Přepište metodu __str__ tak, aby vracela informace o doručovateli, včetně jeho stavu dostupnosti.
        return f"{self.name} je dostupný pro další objednávku."
        


# Vytvoření instance pizzy a manipulace s ní
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)

# Vytvoření instance nápoje
cola = Drink("Cola", 1.5, 500)

# Vytvoření a výpis objednávky
order = Order("Jan Novák", "Pražská 123", [margarita, cola])
print(order)

# Vytvoření řidiče a přiřazení objednávky
delivery_person = DeliveryPerson("Petr Novotný", "777 888 999")
delivery_person.assign_order(order)
print(delivery_person)

# Dodání objednávky
delivery_person.complete_delivery()
print(delivery_person)

# Kontrola stavu objednávky po doručení
print(order)