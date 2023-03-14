from shop.item import Item

class ClassMixin:
    """Миксин класс для Keyboard, хранит и меняет раскладку клавиатуры"""
    def __init__(self, *args, **kwargs):
        self.__language = 'EN'
        super().__init__(*args, **kwargs)

    @property
    def language(self, language='EN'):
        """Превращает атрибут language в свойство"""
        """Возвращает язык клавиатуры"""
        if language == 'EN':
            return self.__language
        else:
            self.__language = language
            return self.__language

    @language.setter
    def language(self, language: str):
        """Если язык раскладки не 'EN' или 'RU'"""
        if language != 'EN' or 'RU':
            raise ValueError('Язык не поддерживается')
        else:
            self.__language = language

    def change_lang(self):
        """Меняет раскладку клавиатуры с 'EN' на 'RU' и обратно"""
        if self.__language.upper() == 'RU':
            self.__language = 'EN'
        else:
            self.__language = 'RU'


class KeyBoard(ClassMixin, Item):
    """Класс, который наследуется от Item и миксин-класса ClassMixin"""
    def __init__(self, name, price, quality) -> None:
        super().__init__(name, price, quality)
        ClassMixin.__init__(self)