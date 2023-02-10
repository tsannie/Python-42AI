from book import Book
from recipe import Recipe

print("Test Recipe:")
tourte = Recipe("Tourte", 1, 10, ["pate", "oeuf", "lardons"], "Préparez en quelques minutes une savoureuse tourte", "lunch")
gateau_chocolat = Recipe("Gateau au chocolat", 2, 30, ["chocolat", "oeuf", "farine"], "Préparez en quelques minutes un délicieux gateau au chocolat", "dessert")

print("Type: " + str(type(tourte)))

print("Errors :")
try:
    tourte = Recipe("", 1, 10, ["pate", "oeuf", "lardons"], "Préparez en quelques minutes une savoureuse tourte", "lunch")
except ValueError as e:
    print(e)

print()
print("Test Book:")

book = Book("My book")

print("creation_date: " + str(book.creation_date))
print("last_update: " + str(book.last_update))

print("add_recipe:")
print("add tourte")
book.add_recipe(tourte)
print("add gateau_chocolat")
book.add_recipe(gateau_chocolat)
print("last_update: " + str(book.last_update))

print("get_recipe_by_name:")
book.get_recipe_by_name("Tourte")

print("get_recipes_by_types:")
recipe_types = book.get_recipes_by_types("dessert")
print(recipe_types)

print("Errors :")
try:
    book.add_recipe(1)
except ValueError as e:
    print(e)




