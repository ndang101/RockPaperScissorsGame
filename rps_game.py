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
  user_input = input("Rock, paper, or scissors? (r,p,s or q to quit playing): ")
  user_pick = user_choice[user_input]

  # Gets computer input
  computer_choice = random.choice(choices)

  # Print user and computer input
  print(f"You chose {choice_emoji[user_pick]}")
  print(f"Computer chose {choice_emoji[computer_choice]}")


  if user_choice[user_input] == computer_choice:
    print("You draw")
  elif win_con[user_pick] == computer_choice:
    print("You win")
  else:
    print("You lose")