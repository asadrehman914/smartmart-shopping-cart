print("================================Wlcome to Shopping Mart===========================================")



from product import Product
from cart import ShoppingCart
from payment import CashPayment

products = [
    Product("Laptop", 85000, 5),
    Product("Phone", 45000, 10),
    Product("Headphones", 3500, 15),
    Product("Watch", 5000, 3),
    Product("Bike", 95000, 7),
    Product("Shoes", 5000, 12),
   
]

cart = ShoppingCart()

while True:
    print("\n1. Show Products")
    print("2. Add to Cart")
    print("3. View Total")
    print("4. Checkout")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        for i, product in enumerate(products, 1):
            print(i, end=". ")
            product.show()

    elif choice == "2":
        number = int(input("Enter product number: "))

        if 1 <= number <= len(products):
            cart.add(products[number - 1])
        else:
            print("Invalid product number")

    elif choice == "3":
        cart.total()

    elif choice == "4":
        if not cart.items:
            print("Cart is empty")
        else:
            amount = sum(p.price for p in cart.items)
            CashPayment().pay(amount)
            cart.items.clear()
            print("Thank you for shopping!")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")

