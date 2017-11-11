#!/usr/bin/python
import time                         # This allows us to access all the functions within the time package

#hello world & current time
print("some python fundamentals")
print ("hello world")   	        # The print() statement will print whatever is enclosed within' its brakets to the console
print (time.strftime("%H:%M"))      # using time we get the current time as a tuple and convert it to a string
