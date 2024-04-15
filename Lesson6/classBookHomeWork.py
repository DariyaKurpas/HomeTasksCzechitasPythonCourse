# Zkus pro nakladatelství vytvořit software s využitím tříd a objektů. Vytvoř tedy třídu Book, která reprezentuje knihu. Každá kniha bude mít atributy title, pages a price. Hodnoty nastav ve funkci __init__.

# Přidej knize funkci get_info(), která vypíše informace o knize v nějakém pěkném formátu.

class Book:
    def __init__(self, title, pages, price, sold, costs):
        self.title = title
        self.pages = pages
        self.price = price
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


book1 = Book("War and Peace", 1100, 599, 20000, 100)

print(book1.getInfo())
print(f"It shall take you approximately {book1.getTimeToRead(2)} hours to read {book1.title}")
print(f"The profit for {book1.sold} pieces of sold {book1.title} is {book1.profit()} CZK. Therefore {book1.title} is {str(book1.rating()).upper()}")



