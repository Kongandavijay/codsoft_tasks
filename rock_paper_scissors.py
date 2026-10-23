
import random

choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0

print("===== ROCK PAPER SCISSORS GAME =====")

while True:
    user = input(
        "\nChoose rock, paper, or scissors (or quit): "
    ).lower().strip()

    if user == "quit":
        break

    if user not in choices:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(choices)

    print("Your choice:", user)
    print("Computer choice:", computer)

    if user == computer:
        print("It's a draw!")

    elif (
        (user == "rock" and computer == "scissors")
        or (user == "paper" and computer == "rock")
        or (user == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    print("Your score:", user_score)
    print("Computer score:", computer_score)

print("\n===== FINAL SCORE =====")
print("Your score:", user_score)
print("Computer score:", computer_score)
print("Thanks for playing!")
