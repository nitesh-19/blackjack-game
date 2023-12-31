import random
from art import logo

def play_blackjack():
    """Starts the game of blackjack"""

    print(logo)
    deck = {
        0: 'A', 1: 2, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7,
        7: 8, 8: 9, 9: 10, 10: 'J', 11: 'Q', 12: 'K',
        13: 'A', 14: 2, 15: 3, 16: 4, 17: 5, 18: 6, 19: 7,
        20: 8, 21: 9, 22: 10, 23: 'J', 24: 'Q', 25: 'K',
        26: 'A', 27: 2, 28: 3, 29: 4, 30: 5, 31: 6, 32: 7,
        33: 8, 34: 9, 35: 10, 36: 'J', 37: 'Q', 38: 'K',
        39: 'A', 40: 2, 41: 3, 42: 4, 43: 5, 44: 6, 45: 7,
        46: 8, 47: 9, 48: 10, 49: 'J', 50: 'Q', 51: 'K',
    }
    computer_hand = []
    player_hand = []
    for card in range(0, 2):
        computer_hand.append(deal_cards(current_deck=deck))
        player_hand.append(deal_cards(current_deck=deck))
    print(f"Your cards: \033[93m{player_hand}\033[0m      Current total = \033[93m{current_score(hand=player_hand)}\033[0m")
    print(f"Computer's first card: \033[93m[{computer_hand[0]}]\033[0m")

    draw_or_pass = "y"
    while draw_or_pass == "y":
        draw_or_pass = input("Type 'y' to get another card or type 'n' to pass: ")
        if draw_or_pass == 'n':
            break
        elif draw_or_pass == 'y':
            player_hand.append(deal_cards(current_deck=deck))
            print(f"Your cards: \033[93m{player_hand}\033[0m      Current total = \033[93m{current_score(hand=player_hand)}\033[0m")
            print(f"Computer's first card: \033[93m[{computer_hand[0]}]\033[0m")
            players_score = current_score(hand=player_hand)
            if players_score > 21:
                print("Bust! Your score overshot, You lose.")
                break
            if players_score == 21:
                print("You Win!")
                break

    while current_score(hand=computer_hand) < 17:
        computer_hand.append(deal_cards(current_deck=deck))
    computers_score = current_score(hand=computer_hand)
    players_score = current_score(hand=player_hand)
    print(f"Your final hand: \033[93m{player_hand}\033[0m      Your Score = \033[93m{players_score}\033[0m")
    print(f"Computer's final hand: \033[93m{computer_hand}\033[0m      Computer's Score = \033[93m{computers_score}\033[0m")
    if players_score > 21:
        print("\033[91mBust! Your score overshot, You lose.\033[0m")
    elif computers_score > 21:
        print("\033[92mBust! Computer's score overshot, You win!\033[0m")
    elif players_score > computers_score or players_score == 21:
        print("\033[91mYou Win!\033[0m")
    elif players_score == computers_score:
        print("\033[91mIt's a Tie!\033[0m")
    else:
        print("\033[91mYou Lose!\033[0m")


def deal_cards(current_deck):
    """Takes input as a dictionary of 52 cards. randomly picks and returns one card without replacement in the
    dictionary. """
    card_no = random.randint(0, 52)
    if card_no not in current_deck:
        return deal_cards(current_deck)
    else:
        dealt_card = current_deck[card_no]
        del current_deck[card_no]
        return dealt_card


def current_score(hand):
    """Takes player's current hand as input and calculates the total score from each card."""
    score = 0
    for element in hand:
        if element == "A":
            score += 11
        elif element == "J" or element == "Q" or element == "K":
            score += 10
        else:
            score += element
        if element == "A" and score > 21:
            score -= 10
    return score


consent = input("Do you want to play blackjack? Type 'y' or 'n'.")
while consent == "y":
    play_blackjack()
    consent = input("Do you want to play blackjack? Type 'y' or 'n'.")
