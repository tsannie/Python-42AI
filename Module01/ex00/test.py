from book import Book
from recipe import Recipe

tourte = Recipe("Tourte", 1, 10, ["pate", "oeuf", "lardons"], "Préparez en quelques minutes une savoureuse tourte", "lunch")
gateau_chocolat = Recipe("Gateau au chocolat", 2, 30, ["chocolat", "oeuf", "farine"], "Préparez en quelques minutes un délicieux gateau au chocolat", "dessert")
to_print = str(tourte)
print(to_print)

book = Book("My book")
book.add_recipe(tourte)
book.get_recipe_by_name("Tourte")
book.get_recipes_by_types("lunch")

book.add_recipe(gateau_chocolat)

