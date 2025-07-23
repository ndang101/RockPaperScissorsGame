import random


# Define user choices
choices = ("r", "p", "s")

# Choice emojis
choice_emoji = {"r": "🪨",
                "p": "📄",
                "s": "✂️"}
# Define win conditions through a library
win_con = {"r": "s",
           "p": "r",
           "s": "p"}

# Function to get the user choice and checks if user input is valid
def get_user_choice():
  while True:
    # Prompt user for input
    user_choice = input("Rock, paper, or scissors? (r,p,s or q): ").lower()

    # If user wants to quit playing
    if user_choice == "q":
      break

    # If user enters invalid input
    if user_choice in choices:
      return user_choice
    else:
      print("Please enter a valid input")



# Game Loop
while True:
  user_choice = get_user_choice()

  # Gets computer input
  computer_choice = random.choice(choices)

  # Print user and computer input as icon
  print(f"You chose {choice_emoji[user_choice]}")
  print(f"Computer chose {choice_emoji[computer_choice]}")

  # If user choice an computer choice are same
  #   then draw
  if choices == computer_choice:
    print("You draw")
  # Otherwise, check the win condition: if the user's choice beats the computer's, the user wins
  elif win_con[user_choice] == computer_choice:
    print("You win")
  # Else computer wins
  else:
    print("You lose")

  # Prompts user if they want to continue after game ends
  # If yes, then continue the loop
  if input("Continue? (y,n): ") == 'y':
    continue
  # Else break the loop and end the game
  else:
    break