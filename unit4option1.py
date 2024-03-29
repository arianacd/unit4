# by ariana daney
# last modified on october 9, 2019
# this program plays blackjack with the user

import random


def get_cards():
    """
    this function generates a random card between 1 and 10
    :return: a random card between 1 and 10
    """
    return random.randint(1, 10)


def print_cards(card1, card2, user_total):
    """
    this function shows the user what their cards are and what their total is
    :param card1: the users first card
    :param card2: the users second card
    :param user_total: the users total
    :return: nothing
    """
    print("you drew a", card1, "and a", card2)
    print("your total is", user_total)


def main():
    card1 = get_cards()
    card2 = get_cards()
    user_total = card1 + card2
    print_cards(card1, card2, user_total)
    another = input("do you want another card? please enter y for yes or n for no")
    if another == "y":
        card3 = get_cards()
        user_total = user_total + card3
        print("you drew a", card3, "and your total is now", user_total)
    if user_total > 21:
        print("your cards are more than 21, you lost so don't go to vegas")
    else:
        card4 = get_cards()
        card5 = get_cards()
        dealer_total = card4 + card5
        print("the dealer drew a", card4, "and a", card5, "so their total is", dealer_total)
        if dealer_total >= user_total:
            print("the dealer won, don't go to vegas")
        else:
            print("you won! go you should go to vegas!")


main()
