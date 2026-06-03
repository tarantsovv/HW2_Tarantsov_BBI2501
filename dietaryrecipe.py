from recipe import Recipe

class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients=None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type

    def scale(self, ratio: float):
        new_recipe = super().scale(ratio)
        new_dietary_recipe = DietaryRecipe(self.title, self.diet_type, new_recipe.ingredients)
        return new_dietary_recipe

    def __str__(self):
        result_ingredients_list = "\n".join(f" - {ingredient}" for ingredient in self.ingredients)
        return f"Блюдо: [{self.diet_type}] {self.title} состоит из следующих элементов: \n {result_ingredients_list}"
