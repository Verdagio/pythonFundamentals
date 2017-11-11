from random import randint          # import random integer function from the random library
#guesing game

selection = 0
number = randint(1, 10)             # set our number to a random number between 1 & 10
wrong = True                        # loop control boolean
while wrong:                        # loop until wrong is set to false
    selection = int(input("Enter a number between 1 - 10: "))       # take input from the user
    if selection == number:
        print("Correct!!")
        wrong = False               # if they guess correctly set wrong to false 
    else:                           # if the user guesses incorrectly we will give a clue 
        if selection > number:
            print("lower")
        elif selection < number:
            print("higher")
