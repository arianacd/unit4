# by ariana daney
# last modified on october 9, 2019
# this program plays blackjack with the user

import random


def get_cards():
    return random.randint(1, 10)


def print_cards(card1, card2, user_total):
    print("you drew a", card1, "and a", card2)
    print("your total is", user_total)


def another_card(card3, new_total):
    another = input("do you want another card? please enter y for yes or n for no")
    if another == "y":
        print("you drew a", card3, "and your total is now", new_total)


def dealer_cards():
    card4 = get_cards()
    card5 = get_cards()
    dealer_total = card4 + card5
    print("the dealer drew a", card4, "and a", card5, "so their total is", dealer_total)


def win_loose(new_total, user_total):
    if new_total > 21 or user_total > 21:
        print("your cards are more than 21, you lost so don't go to vegas")
    else:
        dealer_cards()


def main():
    card1 = get_cards()
    card2 = get_cards()
    user_total = card1 + card2
    print_cards(card1, card2, user_total)
    card3 = get_cards()
    new_total = user_total + card3
    another_card(card3, new_total)
    win_loose(new_total, user_total)



main()
