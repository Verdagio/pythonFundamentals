
#palindrome test

def isPalindrome(string):                   # define a function to check if a word is a palindrome (takes 1 argument)
    res = True                              # this will tell us wether the input word is or isn't a palindrome
    length = len(string)                    # set length to the lenght of the input string

    for i in range(0, int(length/2)):       # loop from 0 -> half the length of the string (only need to loop through half of the string, other half should be the same)
        if string[i] != string[length-i-1]: # if the letter in position i is not equal to the letter in reverse postion
            res = False                     # its not a palindrome
            break                           # stop the loop!
    return print("Result: ", res)           # and return the result


word = input("enter your word: ")           # put in your word
isPalindrome(word)                          # and pop it into the function call!
