# by Ariana Daney
# last modified october 3, 2019
# daily exercises

import random
# exercise 1
number = int(input("chose a number please"))
if (number % 2) == 1:
    print("your number is odd")
else:
    print("your number is even")

# exercise 2


def is_divisible(num1, num2):
    if num1 % num2 == 0:
        return True
    else:
        return False


def is_triangle(a, b, c):
    if (a >= b + c) or (b >= a + c) or (c >= a + b):
        print("these lengths do not make a triangle")
    else:
        print("these lengths make a triangle")


def triangle_input():
    a = int(input("please enter a side length"))
    b = int(input("please enter another a side length"))
    c = int(input("please enter a third a side length"))
    is_triangle(a, b, c)


def computer():
    return random.randint(1, 3)


def rock_paper_scissors(computer_choice):
    print("lets play rock paper scissors!")
    user_choice = int(input("choose 1 for rock, 2 for paper, or 3 for scissors"))
    if user_choice == 1:
        if computer_choice == 1:
            print("the computer chose rock, you tied")
        elif computer_choice == 2:
            print("the computer chose paper, you lost")
        else:
            print("the computer chose scissors, you won")
    elif user_choice == 2:
        if computer_choice == 1:
            print("the computer chose rock, you won")
        elif computer_choice == 2:
            print("the computer chose paper, you tied")
        else:
            print("the computer chose scissors, you lost")
    else:
        if computer_choice == 1:
            print("the computer chose rock, you lost")
        elif computer_choice == 2:
            print("the computer chose paper, you won")
        else:
            print("the computer chose scissors, you tied")


def main():
    number1 = int(input("please give one number"))
    number2 = int(input("please enter another number"))
    if is_divisible(number1, number2):
        print("true")
    else:
        print("false")
    triangle_input()
    computer_choice = computer()
    rock_paper_scissors(computer_choice)


main()
