class Book():
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price

price=int(input("Enter book price:"))
old_price=price/10
after_dis=old_price/10
new_price=price-after_dis
print("new salary after bonus will be:",after_dis)
