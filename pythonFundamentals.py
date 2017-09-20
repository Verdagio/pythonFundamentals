#!/usr/bin/python
import time
from random import randint
import math

#hello world & current time
print("some python fundamentals")
print ("hello world")
print (time.strftime("%H:%M"))

#fizz buzz

i = 0
for i in range(0, 100):
    if (i%3 == 0 and i%5 == 0):
        print("fizzbuzz")
    elif (i%3 == 0):
        print ("fizz")
    elif (i%5 == 0):
        print ("buzz")
    else:
        print (i)
    i+1

#factorial digit sum

def fact(n):

    if n == 0 or n == 1:
        return 1
    else:
        return (n*fact(n-1))


numbers = list(str(fact(100)))
res = 0
n = 0
for number in numbers:
    summed = list(map(int, numbers))
    res += summed[n]
    n+=1

print("Factorial sum Result: ", res)

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

#Largest & smallest in a list

def opposites():
    list = []
    size = int(input("size of list?: "))

    for i in range(size):
        num = int(input("enter numnber: "))
        list.append(num)

    print("Max value: ", max(list), "\nMin value: ", min(list))

opposites()

#palindrome test

def isPalindrome(string):
    res = True
    length = len(string)

    for i in range(0, int(length/2)):
        if string[i] != string[length-i-1]:
            res = False
            break
    return print("Result: ", res)


word = input("enter your word: ")
isPalindrome(word)

#merge & sort lists

def mergeLists():

    list1 = [1, 3, 5]
    list2 = [2, 4, 6]

    fList = list1 + list2

    print("Before: ", str(fList))

    list.sort(fList)

    print("after", str(fList))

mergeLists()

# newtons method for square roots

i = 0
for i in range(0, 5):

    j = i+1
    j_next = j- ((j*j - i) / (2 * j))
    print(str(j_next))
    print(str(math.sqrt(j)))

# reversing a string

def reverseString(string):

    newWord = string[::-1]

    return print("Result: ", newWord)

word = input("enter a word: ")
reverseString(word)



print ("end")