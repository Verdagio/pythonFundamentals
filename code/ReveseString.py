
# reversing a string

def reverseString(string):          # define a function that takes 1 arg

    newWord = string[::-1]          # set the new word to the reverse of the arg see: https://docs.python.org/2.3/whatsnew/section-slices.html

    return print("Result: ", newWord)   # then print it out

word = input("enter a word: ")          # enter a word
reverseString(word)                     # and put it into the method call
