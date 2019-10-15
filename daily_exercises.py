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


def rock_paper_scissors():
    print("lets play rock paper scissors!")
    print("choose rock paper or scissors")
    random.randint(1, 3)
    rock = 1
    paper = 2
    scissors = 3
    if

def main():
    number1 = int(input("please give one number"))
    number2 = int(input("please enter another number"))
    if is_divisible(number1, number2):
        print("true")
    else:
        print("false")
    triangle_input()


main()
