import random

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    player_choice = input("Choose rock, paper, or scissors: ").lower()

    if player_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
    else:
        print(f"Computer chose {computer_choice}")
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("Congratulations! You win!")
        else:
            print("Computer wins. Better luck next time!")

# Start the game
rock_paper_scissors()