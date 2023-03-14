from shop.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        """Инициализирует новый атрибут - number_of_sim"""
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.sim})"

    def __add__(self, other):
        if isinstance(other, Item):
            return self.price + other.price
        else:
            raise ValueError('Количество')

    @property
    def number_of_sim(self, number_of_sim=None):
        """Превращает атрибут number_of_sim в свойство"""
        if number_of_sim == None:
            return self.__number_of_sim
        else:
            self.__number_of_sim = number_of_sim
            return self.__number_of_sim

    @number_of_sim.setter
    def sim(self, number_of_sim: int):
        """Если колличество сим-карт меньше 1, выбрасывает исключение ValueError"""
        if number_of_sim < 1:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        else:
            self.__number_of_sim = number_of_sim