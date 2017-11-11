
#Largest & smallest in a list

def opposites():                            # define a function or method called opposistes that takes no arguments
    list = []                               # create an python list called.. list
    size = int(input("size of list?: "))    # take input for loop control

    for i in range(size):                   # loop to the desired amount
        num = int(input("enter numnber: ")) # enter a number
        list.append(num)                    # add the number to the list

    print("Max value: ", max(list), "\nMin value: ", min(list))     # print out the highest & lowest values in the list

opposites()                                # call the function
