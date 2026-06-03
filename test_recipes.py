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


def test_recipe_creation():
    recipe = Recipe("Пицца Маргарита")
    assert recipe.title == "Пицца Маргарита"
    assert recipe.ingredients == []

def test_recipe_add_ingredient():
    recipe = Recipe("Тесто")
    ingro1 = Ingredient("Мука", 200.0, "г")
    ingro2 = Ingredient("Мука", 300.0, "г")
    ingro3 = Ingredient("Вода", 100.0, "мл")
    
    recipe.add_ingredient(ingro1)
    assert len(recipe) == 1
    recipe.add_ingredient(ingro2)
    assert len(recipe) == 1
    assert recipe.ingredients[0].quantity == 500.0
    recipe.add_ingredient(ingro3)
    assert len(recipe) == 2

def test_recipe_scale():
    recipe = Recipe("Соус")
    recipe.add_ingredient(Ingredient("Томаты", 2.0, "шт"))
    scaled = recipe.scale(3.0)
    assert scaled is not recipe
    assert scaled.ingredients[0].quantity == 6.0
    assert recipe.ingredients[0].quantity == 2.0