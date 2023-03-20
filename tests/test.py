import pytest

from shop.item import Item
from shop.phone import Phone
from shop.keyboard import KeyBoard
import os
from errors.errors import InstantiateCSVError

def test_item_init():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv('test.csv')
    assert len(Item.all) == 5
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.0) is True
    assert Item.is_integer(5.5) is False


def test_repr_str():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == repr(Item("Смартфон", 10000, 20))
    assert str(item1) == "Смартфон"

def test_cls_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_cls_keyboard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == 'Dark Project KD87A'
    assert str(kb.language) == 'EN'
    kb.change_lang()
    assert str(kb.language) == 'RU'

def test_file_not_found_error():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('../items.csv')

def test_instantiate_csv_error():
    assert Item.instantiate_from_csv('../items.csv') == print("Файл item.csv поврежден")