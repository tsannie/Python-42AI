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
        print(recipe)

def print_recipe(recipe_name):
    print("Recipe for " + recipe_name + ":")
    print("Ingredients list: " + str(cookbook[recipe_name]["ingredients"]))
    print("To be eaten for " + cookbook[recipe_name]["meal"] + ".")
    print("Takes " + str(cookbook[recipe_name]["prep_time"]) + " minutes of cooking.")

def delete_recipe(recipe_name):
    del cookbook[recipe_name]

def add_recipe():
    recipe_name = input("Enter a name: ")
    ingredients = []
    print("Enter ingredients (or nothing to stop):")
    while True:
        ingredient = input("- ")
        if ingredient == "":
            break
        ingredients.append(ingredient)
    meal = input("Enter a meal type: ")
    prep_time = input("Enter a preparation time: ")
    cookbook[recipe_name] = {"ingredients": ingredients, "meal": meal, "prep_time": prep_time}

def options_list():
    print("List of available option:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit\n")

# main
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
