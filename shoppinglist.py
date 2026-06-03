from ingredient import Ingredient
from recipe import Recipe

class ShoppingList:
    def __init__(self):
        self._items = []
    
    def add_recipe(self, recipe:Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        else:
            new_recipe = recipe.scale(portions)
            for ingredient in new_recipe.ingredients:
                self._items.append((ingredient, new_recipe.title))
            return
    
    def remove_recipe(self, title:str):
        self._items = [ingredient for ingredient in self._items if ingredient[1] != title]
        
    def get_list(self):
        final_shoplist = {}
        for ingredient, recipe_title in self._items:
            key = (ingredient.name, ingredient.unit)
            final_shoplist[key] = final_shoplist.get(key, 0) + ingredient.quantity
        result = []
        for (name, unit), quantity in final_shoplist.items():
            result.append(Ingredient(name, quantity, unit))
        result.sort(key=lambda x: x.name)
        return result
    
    def __add__(self, other):
     merged_list = ShoppingList()
     merged_list._items = self._items + other._items
     return merged_list

