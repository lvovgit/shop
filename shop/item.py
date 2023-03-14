import csv
import os
from errors.errors import InstantiateCSVError


class Item:
    pay_rate = 0  # коэффициент скидки, изначально равен 0
    copy_amount = 0
    all = []

    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)
        Item.copy_amount += 1

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', '{self.price}', '{self.quantity}')"

    def __str__(self):
        return f'{self.name}'

    @classmethod
    def instantiate_from_csv(cls, path: str):
        """"Считывает данные из csv-файла и создает экземпляры класса, инициализируя их данными из файла"""
        """Если файл не найден или поврежден выбрасывает соответствующие Exception"""

        if not os.path.isfile("../items.csv"):
            raise FileNotFoundError("отсутствует файл")
        try:
            with open(path, encoding='windows-1251') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if list(row.keys()) == ['name', 'price', 'quantity']:
                        cls(name=row['name'], price=float(row['price']), quantity=int(row['quantity']))
                    else:
                        raise InstantiateCSVError

        except KeyError:
            InstantiateCSVError('Файл items.csv поврежден')

    @staticmethod
    def is_integer(number):
        """Проверка, является ли число целочисленным"""
        if number % 1 == 0:
            return True
        else:
            return False

    def calculate_total_price(self):
        """Получает общую стоимость конкретного товара в магазине"""
        return self.price * self.quantity

    def apply_discount(self):
        """Применяет установленную скидку для конкретного товара"""
        self.price = self.price * self.pay_rate
        return self.price

    @property
    def name(self):
        """Превращает навзвание товара в свойство, взвращает название товара"""
        return self.__name

    @name.setter
    def name(self, value: str):
        """Делает проверку длины названия товара"""
        if len(value) <= 10:
            self.__name = value
        else:
            print('Exception: Длина товара превышает допустимую длину')


# item1 = Item("Смартфон", 10000, 20)
# item2 = Item("Ноутбук", 20000, 5)
#
# print(item1.calculate_total_price())
# print(item2.calculate_total_price())
#
# Item.pay_rate = 0.8
# item1.apply_discount()
#
# print(item1.price)
# print(item2.price)
#
# print(Item.all)

# item = Item('Телефон', 10000, 5)
# item.name = 'Смартфон'
# print(item.name)

# item.name = 'СуперСмартфон'
Item.instantiate_from_csv('../items.csv')
# print(len(Item.all))
# item1 = Item.all[0]
# print(item1.name)

# print(Item.is_integer(5))
# print(Item.is_integer(5.0))
# print(Item.is_integer(5.5))

# item1 = Item("Смартфон", 10000, 20)
# item1

# phone1 = Phone("iPhone 14", 120_000, 5, 2)

# kb = KeyBoard('Dark Project KD87A', 9600, 5)
# print(kb)
# print(kb.language)
# kb.change_lang()
# print(kb.language)
# print(KeyBoard.mro())
# kb.language = 'CH'
