# Zkus pro nakladatelství vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Book, která reprezentuje knihu. Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.

# Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.

class Item:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def getTimeToRead(self):
        pass

class Book(Item):
    def __init__(self, title, pages, price, sold = 0, costs = 0):
        super().__init__(title, price)
        self.pages = pages
        self.sold = sold
        self.costs = costs
    # Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.

    def getInfo(self):
        return f"Our newest arrival {self.title} is a pretty decent book with {self.pages} pages at a cost of only {self.price} CZK."
    # Přidej metodu get_time_to_read(). Metoda vrátí čas potřebný na přečtení knihy v hodinách. S využitím atributu pages vypočítej čas na přečtení knihy. 
    # Metoda bude mít nepovinný parametr, který udává počet minut potřebných pro přečtení jedné stránky knihy. 
    # Dobu potřebnou na přečtení knihy získáš jako násobek doby potřebné na přečtení jedné stránky knihy a počet stránek knihy. 
    # Výchozí hodnota nepovinného parametru je 4.

    def getTimeToRead(self,timeForOnePageInMinutes=4):
        timeToReadInHours = round(timeForOnePageInMinutes * self.pages / 60, 1)
        return timeToReadInHours
    
    # Přidej metodu profit(), která vrátí celkový zisk z knihy. Zisk vypočti na základě vzorce: prodané kusy * (cena - náklady).
    def profit(self):
        profitOneTitle = self.sold * (self.price - self.costs)
        return profitOneTitle
    
    # Přidej metodu rating(), která vrátí hodnocení knihy na základě jejího zisku. Pokud bude zisk méně než 50 tisíc, vrať hodnotu "propadák". 
    # Pokud bude zisk mezi 50 tisíc a 500 tisíc, vrať hodnotu "průměr". Pokud bude vyšší než 500 tisíc, vrať hodnotu "bestseller".
    def rating(self):
        profit = self.profit()
        if profit < 50000:
            return "fail"
        elif profit < 500000:
            return "average"
        else:
            return "bestseller"
        
class AudioBook(Item):
    def __init__(self, title, price, duration_in_hours, narrator):
        super().__init__(title, price)
        self.duration_in_hours = duration_in_hours
        self.narrator = narrator
    
    def getTimeToRead(self):
        return self.duration_in_hours
    
    def getInfo(self):
        return f"Our newest arrival {self.title} is a pretty decent book, that will take you {self.duration_in_hours} hours to read at a cost of only {self.price} CZK."


book1 = Book("War and Peace", 599, 1100, 20000, 100)
book2_audio = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Horák")
book3 = Book("Kadet Hornblower", 399, 242)

# print(book1.getInfo())
# print(f"It shall take you approximately {book1.getTimeToRead(2)} hours to read {book1.title}")
# print(f"The profit for {book1.sold} pieces of sold {book1.title} is {book1.profit()} CZK. Therefore {book1.title} is {str(book1.rating()).upper()}")

# print(book2_audio.getInfo())

# total_time = book1.getTimeToRead() + book2_audio.getTimeToRead()

# print(f"It will take you in total {total_time} to explore your new books, {book1.title} and {book2_audio.title}. Enjoy!")

favourite_narrator = "Zbyšek Horák"
item_1 = AudioBook("Problém tří těles", 299, 14.4, "Zbyšek Horák")
item_2 = Book("Kadet Hornblower", 399, 242)
item_3 = AudioBook("Odysseus", 389, 13.7, "Lukáš Hlavica")

all_items = [item_1, item_2, item_3]

for item in all_items:
    if hasattr(item, "narrator"):
        if item.narrator == "Zbyšek Horák":
            print(item.title)


