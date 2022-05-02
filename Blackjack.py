import random

def deal_card():
  '''deals a card at random'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def total_score(cards):
  if sum(cards) == 11 and len(cards) == 2:
    return 0
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare_scores(player_score, computer_score):
  if player_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, your opponent has blackjack. Better luck next time!"
  elif player_score == 0:
    return "You win with a blackjack!"
  elif player_score > 21:
    return "You went over, you lose. Better luck next time!"
  elif computer_score > 21:
    return "Opponent went over, you win!"
  elif player_score > computer_score:
    return "You win!"
  else:
    "You lose, better luck next time!"

def play_game():

  player_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2): #Player card deal
    new_card = deal_card()
    player_cards.append(new_card)#
  for _ in range(2): #Computer card deal
    new_card = deal_card()
    computer_cards.append(new_card)

  while not is_game_over:
    player_score = total_score(player_cards)
    computer_score = total_score(computer_cards)
    print(f"Your cards are: {player_cards}, meaning your current total is {player_score}")
    print(f"The computer's first card is: {computer_cards[0]}")

    if player_score == 0 or computer_score == 0 or player_score > 21:
      is_game_over = True
    else:
      continue_playing = input("Type 'y' to get another card, type 'n' to pass:\n").lower()
      if continue_playing == 'y':
        player_cards.append(deal_card())
        player_score = total_score(player_cards)
      else:
        is_game_over = True

  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = total_score(computer_cards)

  print(f"Your final hand is: {player_cards} and your final score is {player_score}")
  print(f"The opponent's final hand is {computer_cards} and their final score is {computer_score}")
  print(compare_scores(player_score, computer_score))

while input("Would you like to play a game of blackjack? Press 'y' or 'n'\n").lower() == 'y':
  play_game()