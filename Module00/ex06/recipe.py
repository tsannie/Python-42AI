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

def print_recipe_names():
    print("Recipes:")
    for recipe in cookbook:
        print("- ", recipe)

def print_recipe(recipe_name):
    if recipe_name not in cookbook:
        print("Sorry, this recipe does not exist in the cookbook.")
        return
    print("Recipe for " + recipe_name + ":")
    print("Ingredients list: " + str(cookbook[recipe_name]["ingredients"]))
    print("To be eaten for " + cookbook[recipe_name]["meal"] + ".")
    print("Takes " + str(cookbook[recipe_name]["prep_time"]) + " minutes of cooking.")

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        print("Recipe for " + recipe_name + " deleted.")
        del cookbook[recipe_name]
    else:
        print("Sorry, this recipe does not exist in the cookbook.")

def add_recipe():
    while 42:
        recipe_name = input("Enter a name: ")
        if recipe_name in cookbook:
            print("Sorry, this recipe already exists in the cookbook.")
            continue
        if isinstance(recipe_name, str) and recipe_name != "":
            break
        print("Sorry, this is not a valid name.")
    print("Enter ingredients (or nothing to stop):")

    ingredients = []
    while 42:
        ingredient = input("- ")
        if ingredient == "":
            if len(ingredients) == 0:
                print("Sorry, you must enter at least one ingredient.")
                continue
            break
        if ingredient in ingredients:
            print("Sorry, this ingredient already exists in the recipe.")
            continue
        ingredients.append(ingredient)

    while 42:
        meal = input("Enter a meal type: ")
        if isinstance(meal, str) and meal != "" and not all(c.isdigit() for c in meal):
            break
        print("Sorry, this is not a valid meal type.")

    while 42:
        prep_time = input("Enter a preparation time: ")
        try:
            prep_time = int(prep_time)
            if prep_time > 0:
                break
        except ValueError:
            pass
        print("Sorry, this is not a valid preparation time.")
    cookbook[recipe_name] = {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}

def options_list():
    print("\nList of available option:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit\n")

if __name__ == "__main__":
    print("Welcome to the Python Cookbook !")
    options_list()

    while True:
        choice = input("Please select an option by typing the corresponding number: \n>>> ")
        if choice == "1":
            add_recipe()
        elif choice == "2":
            recipe_name = input("Enter a recipe name: ")
            delete_recipe(recipe_name)
        elif choice == "3":
            recipe_name = input("Please enter a recipe name to get its details: ")
            print_recipe(recipe_name)
        elif choice == "4":
            print_recipe_names()
        elif choice == "5":
            break
        else:
            print("Sorry, this option does not exist.")
        options_list()
        print("")

    print("Cookbook closed. Goodbye !")
