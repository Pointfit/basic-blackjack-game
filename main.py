import random
from replit import clear
from art import logo
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
game_running = True

while game_running:
  print(logo)
  user_cards = [deal_card(), deal_card()]
  computer_cards = [deal_card(), deal_card()]
  
  def calculate_score(list_of_cards):
    if sum(list_of_cards) == 21:
      return 0
    if 11 in list_of_cards and sum(list_of_cards) > 21:
      list_of_cards.remove(11)
      list_of_cards.append(1)
    return sum(list_of_cards)


  def check():
    while True:
      print(f"Your cards: {user_cards}, current score : {sum(user_cards)}")
      print(f"Computer's first card: {computer_cards[0]}")
      if calculate_score(user_cards) == 0:
        print("You win")
        return False
      elif calculate_score(computer_cards) == 0 or calculate_score(user_cards) > 21:
        print("You lose")
        return False
      elif input("Do you want to draw another card? ").lower() == "yes":
        user_cards.append(deal_card())
        if calculate_score(user_cards) > 21:
          print("You went over. You lose.")
          return False
      else:
        return True

  check()
  
  while sum(computer_cards) < 17:
    computer_cards.append(deal_card())
    while 11 in computer_cards and sum(computer_cards) > 21:
      computer_cards.remove(11)
      computer_cards.append(1)
  
  def compare(user_score, computer_score):
    if user_score == computer_score:
      print("It's a draw")
    elif computer_score == 0:
      print("You lose")
    elif user_score == 0:
      print("You win")
    elif user_score > 21:
      print("You lose")
    elif computer_score > 21:
      print("You win")
    elif user_score > computer_score:
        print("You win")
    else:
        print("You lose")

  print("Your final hand:", user_cards)
  print("Your final score:", calculate_score(user_cards))
  print("Computer's final hand:", computer_cards)
  print("Computer's final score:", calculate_score(computer_cards))
  compare(calculate_score(user_cards), calculate_score(computer_cards))

  play_again = input("Do you want to play again? ").lower()
  if play_again != "yes":
      game_running = False
  clear()