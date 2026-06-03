import pytest

from recipe import Recipe
from shoppinglist import ShoppingList
from ingredient import Ingredient
from dietaryrecipe import DietaryRecipe

def test_ingredient_initialisation():
    ingro = Ingredient("Мука", 500, "грамм")
    assert ingro.name == "Мука"
    assert ingro.quantity == 500.0
    assert ingro.unit == "грамм"

def test_ingredient_str():
    ingro = Ingredient("Мука", 500, "грамм")
    assert str(ingro) == "Мука: 500.0 грамм"

def test_ingredient_eq():
    ingro1 = Ingredient("Мука", 500, "грамм")
    ingro2 = Ingredient("Мука", 300, "грамм")
    ingro3 = Ingredient("Перец", 500, "грамм")
    ingro4 = Ingredient("Мука", 300, "килограмм")

    assert ingro1 == ingro2
    assert ingro1 != ingro3
    assert ingro2 != ingro4