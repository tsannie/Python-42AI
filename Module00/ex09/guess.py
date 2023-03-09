import random

def found(attempts, secret):
      if secret == 42:
          print("The answer to the ultimate question of life, the universe and everything is 42.")
      if attempts == 1:
          print("Congratulations! You got it on your first try!")
      else:
          print("Congratulations, you've got it!")
          print("You won in {} attempts!".format(attempts))

def guess():
    secret = random.randint(1, 99)
    attempts = 0
    while True:
        print("What's your guess between 1 and 99?")
        guess = input(">> ")
        if guess == "exit":
            print("Goodbye!")
            break

        try:
            guess = int(guess)
        except ValueError:
            print("That's not a number.")
            continue

        attempts += 1
        if guess == secret:
            found(attempts, secret)
            break
        elif guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")

if __name__ == '__main__':
    print("This is an interactive guessing game!")
    print("You have to enter a number between 1 and 99 to find out the secret number.")
    print("Type 'exit' to end the game. Good luck!")
    print()
    guess()
