# Vytvoř třídu Ticket, která bude mít atributy basic_price (základní cena) a seat_number (číslo sedadla). Tato třída bude sloužit například pro cesty autobusem.

class Ticket:
    def __init__(self, basic_price: str, seat_number: str):
        self.basic_price = basic_price
        self.seat_number = seat_number

# Při cestování vlakem musíme řešit, jestli cestující využívá 1. nebo 2. třídu. Vytvoř třídu TrainTicket, 
# která bude mít navíc atribut fare_class (uvažujeme možnosti economy a business). Dále naprogramuj metodu get_price(), 
# která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy, a cenu o 30 % vyšší oproti basic_price, pokud fare_class je business.

class TrainTicket(Ticket):
    def __init__(self, basic_price: float, seat_number: str, fare_class: str):
        super().__init__(basic_price, seat_number)
        self.fare_class = fare_class
    
    def get_price(self):
        if self.fare_class == "economy":
            return self.basic_price
        elif self.fare_class == "business":
            return self.basic_price * 1.3 # 30% more expensive ticket
        else:
            return f"The fare class {self.fare_class} doesn't exist. Please try again."
        
# U letenek řešíme třídu, kterou cestující letí, navíc ale musíme řešit i počet odbavených zavazadel. 
# Vytvoř třídu PlaneTicket, která bude dědit od třídy TrainTicket a bude mít navíc atribut checkout_luggages, který udává počet odbavených zavazadel. 
# Naprogramuj metodu get_price(), která bude vracet hodnotu stejnou jako basic_price, pokud atribut fare_class je economy, a cenu o 50 % vyšší oproti basic_price, 
# pokud fare_class je business. Dále připočti 2000 za každé odbavené zavazadlo (bez ohledu na třídu).

class PlaneTicket(TrainTicket):
    def __init__(self, basic_price: float, seat_number: str, fare_class: str, checkout_luggage: int):
        super().__init__(basic_price, seat_number, fare_class)
        self.checkout_luggage = checkout_luggage
    
    def get_price(self):
        if self.fare_class == "economy":
            extra_fare_for_luggage = 2000 * self.checkout_luggage
            return self.basic_price + extra_fare_for_luggage
        elif self.fare_class == "business":
            extra_fare_for_luggage = 2000 * self.checkout_luggage
            return self.basic_price * 1.5 # 50% more expensive ticket
        else:
            return f"{self.fare_class} fare class is unknown. Please try again"
    
ticket1_train_business = TrainTicket(300, 46, "business")
ticket2_train_economy = TrainTicket(300, 47, "economy")
ticket3_train_error = TrainTicket(300, 45, "error")
ticket4_plane_business = PlaneTicket(6000, "1A", "business", 0)
ticket5_plane_economy = PlaneTicket(6000, "5G", "economy", 0)
ticket6_plane_error = PlaneTicket(6000, "12H", "error", 2)
print(f"The price for this ticket is {round(ticket1_train_business.get_price())}.")
print(f"The price for this ticket is {ticket2_train_economy.get_price()}.")
print(f"The price for this ticket is {ticket3_train_error.get_price()}.")
print(ticket4_plane_business.get_price())
print(ticket5_plane_economy.get_price())
print(ticket6_plane_error.get_price())


combinedTicket = ticket1_train_business.get_price() + ticket4_plane_business.get_price() * 2 + ticket2_train_economy.get_price() * 10 + ticket5_plane_economy.get_price() * 20

print(combinedTicket)



