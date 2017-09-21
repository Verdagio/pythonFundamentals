
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
