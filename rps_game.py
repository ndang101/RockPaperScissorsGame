import random
import emoji

# Define choices
choices = ["rock", "paper", "scissors"]
# Define user choices
user_choice = {"r": "rock",
           "p": "paper",
           "s": "scissors"}

# Choice emojis
choice_emoji = {"rock": "🪨",
                "paper": "📄",
                "scissors": "✂️",
                "r": "🪨",
                "p": "📄",
                "s": "✂️"}
# Define win conditions through a library
win_con = {"rock": "scissors",
           "paper": "rock",
           "scissors": "paper"}

# Game Loop
while True:

  
  # Prompt user for input
  user_input = input("Rock, paper, or scissors? (r,p,s or q to quit playing): ").lower()


  # If user wants to quit playing
  if user_input == "q":
    break

  # If user enters invalid input
  if user_input not in user_choice:
    print("Please enter a valid input")
    continue

  # Change input into response
  user_pick = user_choice[user_input]

  # Gets computer input
  computer_choice = random.choice(choices)

  # Print user and computer input as icon
  print(f"You chose {choice_emoji[user_pick]}")
  print(f"Computer chose {choice_emoji[computer_choice]}")

  # If user choice an computer choice are same
  #   then draw
  if user_choice[user_input] == computer_choice:
    print("You draw")
  # Otherwise, check the win condition: if the user's choice beats the computer's, the user wins
  elif win_con[user_pick] == computer_choice:
    print("You win")
  # Else computer wins
  else:
    print("You lose")