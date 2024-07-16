"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import *

def test_calculate_total_price():
    item = Item("Наушники", 5000, 5)
    assert item.calculate_total_price() == 25000

def test_apply_discount():
    item = Item("Наушники", 5000, 5)
    item.apply_discount()
    assert item.price == item.price
