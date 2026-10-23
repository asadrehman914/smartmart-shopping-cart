
class ShoppingCart:
    def __init__(self):
        self.items = []

    def add(self, product):
        if product.stock > 0:
            self.items.append(product)
            product.stock -= 1
            print(product.name, "added to cart")
        else:
            print("Product out of stock")

    def total(self):
        amount = 0
        for product in self.items:
            amount += product.price
        print("Total: PKR", amount)
