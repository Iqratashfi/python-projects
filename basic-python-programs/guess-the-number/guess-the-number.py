import random

name = input("Heyyy, what's your name?")
print("Welcome to the game " + name)

play_again = "yes"

while play_again == "yes":
    secret_num = random.randint(1, 100)
    guess = 0
    attempts = 0

    while guess != secret_num:
        guess = input("Guess a number between 1 and 100: ")
        guess = int(guess)
        attempts += 1

        if guess == secret_num:
            print("You guessed it right!!!!")
        elif guess > secret_num:
            print("Too high!Try again!")
        else:
            print("Too low!Try again!")

    print("Attempsts: ", attempts)

    play_again = input("Would you like to play again? (yes/no): ")
    if play_again == "no":
      print("Thank you for playing!" +name+ "!!!")
