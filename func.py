class Item:
    pay_rate = 0
    copy_amount = 0
    all = []

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.all += (self, name, price, quantity)

        Item.copy_amount += 1

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate
        return self.price


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)

print(item1.calculate_total_price())
print(item2.calculate_total_price())

Item.pay_rate = 0.8
item1.apply_discount()

print(item1.price)
print(item2.price)

print(Item.all)