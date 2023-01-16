cookbook= {
  "sandwich": {
    "ingredients": [ "ham", "bread", "cheese", "tomatoes" ],
    "meal": "lunch",
    "prep_time": 10
  },
  "cake": {
    "ingredients": [ "flour", "sugar", "eggs" ],
    "meal": "dessert",
    "prep_time": 60
  },
  "salad": {
    "ingredients": [ "avocado", "arugula", "tomatoes", "spinach" ],
    "meal": "lunch",
    "prep_time": 15
  }
}

# print all recipe names
def print_recipe_names():
    print("Recipes:")
    for recipe in cookbook:
        print(recipe)

# takes a recipe name and print its details
def print_recipe(recipe_name):
    print("Recipe for " + recipe_name + ":")
    print("Ingredients list: " + str(cookbook[recipe_name]["ingredients"]))
    print("To be eaten for " + cookbook[recipe_name]["meal"] + ".")
    print("Takes " + str(cookbook[recipe_name]["prep_time"]) + " minutes of cooking.")

# takes a recipe name and delete it.
def delete_recipe(recipe_name):
    del cookbook[recipe_name]

# add a recipe from user input.
def add_recipe():
    recipe_name = input("Enter a name: ")
    ingredients = input("Enter ingredients: ").split()
    meal = input("Enter a meal type: ")
    prep_time = input("Enter a preparation time: ")
    cookbook[recipe_name] = {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}
