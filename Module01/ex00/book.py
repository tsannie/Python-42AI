from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name):
        """Constructor of the class"""

        if name == "" or type(name) != str:
            raise ValueError("Invalid name")
        self.name = name

        self.last_update = datetime.now()
        self.creation_date = datetime.now()
        self.recipes_list = {
            'starter': [],
            'lunch': [],
            'dessert': [],
        }


    def get_recipe_by_name(self, name):
        """Prints a recipe with the name \texttt{name} and returns the instance"""
        #... Your code here ...
        for recipe_type in self.recipes_list:
            for recipe in self.recipes_list[recipe_type]:
                if recipe.name == name:
                    print(recipe)
                    return recipe
        print(name + " not found")
        return None


    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        #... Your code here ...
        if recipe_type not in self.recipes_list:
            return []
        return [recipe.name for recipe in self.recipes_list[recipe_type]]

    def add_recipe(self, recipe):
        """Add a recipe to the book and update last_update"""
        #... Your code here ...
        if type(recipe) != Recipe:
            raise ValueError("Invalid recipe")
        if recipe.recipe_type not in self.recipes_list:
            return
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

