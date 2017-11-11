#fizz buzz

i = 0                               # initialize i to 0
for i in range(0, 100):             # run a loop from 0 -> 100
    if (i%3 == 0 and i%5 == 0):     # if the remainder of i is 0 when diveded by 3 & by 5
        print("fizzbuzz")           # printout fizzbuzz!
    elif (i%3 == 0):                # otherwise if the remainder of i is 0 when divided by just 3
        print ("fizz")              # print fizz
    elif (i%5 == 0):                # otherwise if theremainder of i is 0 when divided by just 5
        print ("buzz")              # print buzz
    else:                           # finally if it doesn't meet any of the past requirements                
        print (i)                   # just print the number
    i+1                             # and increment i by 1