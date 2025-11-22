# import random

def guess_number():
    ans = 67
    bot = int(input("Guess a number between 1 and 100: "))
    
    while bot != ans:
        if bot > ans:
            bot = int(input("Too high! Try again: "))
        else:
            bot = int(input("Too low! Try again: "))
    
    print("That is the right answer!")

guess_number()
