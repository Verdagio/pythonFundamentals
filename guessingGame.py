from random import randint
#guesing game

selection = 0
number = randint(1, 10)
wrong = True
while wrong:
    selection = int(input("Enter a number between 1 - 10: "))
    if selection == number:
        print("Correct!!")
        wrong = False
    else:
        if selection > number:
            print("lower")
        elif selection < number:
            print("higher")
