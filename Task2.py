print("\n=========================ROCK PAPER SCISSOR GAME========================\n")

#Import Random Module for selecting options
import random

# Player Score
Player_Score = 0
# Computer Score
Computer_Score = 0
#rounds
round=1

# A Tuple of options to be selected by Player and Computer
options = ("rock", "paper", "scissors")

# Function for Player's Choice
def get_player_choice():
    player_choice= None
    while player_choice not in options:
        player_choice = input("Enter a choice (Rock, Paper, Scissors): ").lower()
        if player_choice not in options:
            print("Invalid choice. Please try again.")
    print(f"Player: {player_choice}")
    return player_choice

# GAME ROUNDS
while round<=3:
    print(f"Round {round}")
    player_choice = get_player_choice()
    computer_choice = random.choice(options)
    print(f"Computer: {computer_choice}")

    if player_choice == computer_choice:
        print("It's a TIE!\n")
    elif (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        print("\nYou WIN!\n")
        Player_Score += 1
    else:
        print("\nYou LOSE!\n")
        Computer_Score += 1
    round+=1

#COUNTING SCORES
print("Your Total Score:", Player_Score)
print("Computer Total Score:", Computer_Score, "\n")

if Player_Score > Computer_Score:
    print("Congratulations!! You are the WINNER of this GAME.\n")
elif Player_Score < Computer_Score:
    print("Sorry!! You have LOST in this GAME.\n")
else:
    print("It is a TIE.\n")

print("Thanks for Playing!")

print("\n=========================GAME ENDED========================\n")