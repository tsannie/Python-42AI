

class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        """Constructor of the class"""

        if name == "" or type(name) != str:
            raise ValueError("Invalid name")
        self.name = name

        if cooking_lvl < 1 or cooking_lvl > 5 or type(cooking_lvl) != int:
            raise ValueError("Invalid cooking level")
        self.cooking_lvl = cooking_lvl

        if cooking_time < 0 or type(cooking_time) != int:
            raise ValueError("Invalid cooking time")
        self.cooking_time = cooking_time

        if type(ingredients) != list or len(ingredients) == 0:
            raise ValueError("Invalid ingredients")
        self.ingredients = ingredients

        if type(description) != str:
            raise ValueError("Invalid description")
        self.description = description

        if recipe_type != "starter" and recipe_type != "lunch" and recipe_type != "dessert":
            raise ValueError("Invalid recipe type")
        self.recipe_type = recipe_type


    def __str__(self):
        """Return the string to print with the recipe info"""
        """Your code here"""
        txt = "Recipe name: " + self.name + "\n"
        txt += "Cooking level: " + str(self.cooking_lvl) + "\n"
        txt += "Cooking time: " + str(self.cooking_time) + "\n"
        txt += "Ingredients: " + str(self.ingredients) + "\n"
        txt += "Description: " + self.description + "\n"
        txt += "Recipe type: " + self.recipe_type + "\n"
        return txt

