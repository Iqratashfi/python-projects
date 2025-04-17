import random
name = input("Enter your name: ")

choices = ['rock', 'paper', 'scissors']
user_score = 0
computer_score = 0

while True:
    choice = input("what do u choose(rock, paper, scissors)?")
    if choice not in choices:
        print("wrong choice. Pick rock, paper or scissors")
        continue

    choice2 = random.choice(choices)
    if choice == choice2:
        print("You both chose the same. Play again")
    elif choice == "rock" and choice2 == "scissors":
        print("Rock beats Scissors " +name+ " YOU WON")
        user_score += 1
    elif choice =="paper" and choice2 == "rock":
        print("paper beats rock " +name+ " YOU WON")
        user_score += 1
    elif choice =="scissors" and choice2 == "paper":
        print("Scissors beats paper " +name+ " YOU WON")
        user_score += 1
    else:
        print(f" {choice2} beats {choice}. YOU LOSE")
        computer_score += 1
    print(f"{name} score: {user_score} Computer:{computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
  
    if play_again == "no":
        print("Final Score")
        print(f"{name}:{user_score} and Computer:{computer_score}")
        print("Thank you for playing!Come back soon!")
        break
