from ingredient import Ingredient
class Recipe:
    def __init__(self, title = "", ingredients = None):
        self.title = title
        self.ingredients = ingredients if ingredients is not None else []
    
    def add_ingredient(self, ingredient: Ingredient):
        found = False
        for ingredient_val in self.ingredients:
            if ingredient_val == ingredient:
                ingredient_val.quantity = ingredient_val.quantity + ingredient.quantity
                found = True
                break
        if not found:
            self.ingredients.append(ingredient)

    @staticmethod
    def is_valid_ratio(ratio):
        try:
            ratio = float(ratio)
        except Exception:
            return False
        else: 
            if ratio > 0:
                return True
            else:
                return False
    
    def scale(self, ratio: float):
        if ratio <= 0:
            raise ValueError("Количество должно быть положительным")
        new_recipe = Recipe(self.title)
        for val in self.ingredients:
            new_quantity = val.quantity * ratio
            new_ingredient = Ingredient(val.name, new_quantity, val.unit)
            new_recipe.add_ingredient(new_ingredient)
        return new_recipe
    
    def __len__(self):
        return len(self.ingredients)
    
    def __str__(self):
        result_ingredients_list = "\n".join(f" - {ingredient}" for ingredient in self.ingredients)
        return f"Блюдо: {self.title} состоит из следующих элементов: \n {result_ingredients_list}"
