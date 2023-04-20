import random

def get_choices():
  player_choice = input("Enter a choice(rock, paper, scissors): ")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)

  choices = {"player": player_choice, "computer": computer_choice}
  return choices

def check_win(player, computer):
  print(f"You chose {player}, Computer chose {computer}")
  if player == computer:
    return "Draw" 

  elif player == "rock":
    if computer == "scissors":
      return "player wins"
    else:
      return "computer wins"

  elif player == "paper":
    if computer == "rock":
      return "player wins"
    else:
      return "computer wins"

  elif player == "scissors":
    if computer == "paper":
      return "player wins"
    else:
      return "computer wins"
  
  return[player, computer]

choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)