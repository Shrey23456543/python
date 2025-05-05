class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self, discount_percentage):
        discount_amount = self.price * (discount_percentage / 100)
        self.price -= discount_amount
        return self.price

book1 = Book("The odyssey of kashmiri pandits", "M.L.bhaat", 500)
print(f"Original Price of '{book1.title}': ₹{book1.price}")
new_price = book1.apply_discount(20)
print(f"Price after 20% discount: ₹{new_price}")
