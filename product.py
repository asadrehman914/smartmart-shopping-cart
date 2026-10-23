
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def show(self):
        print(self.name, self.price, self.stock)
