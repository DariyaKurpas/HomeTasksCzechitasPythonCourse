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

