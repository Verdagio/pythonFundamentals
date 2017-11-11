
#merge & sort lists

def mergeLists():                   # define a function called mergeLists that takes no arguments

    list1 = [1, 3, 5]               # create a list with some values
    list2 = [2, 4, 6]               # and another 

    fList = list1 + list2           # combine both lists into one

    print("Before: ", str(fList))   # print it out before sorting

    list.sort(fList)                # sort the list lowest value to highes by default

    print("after", str(fList))      # print it out after sorting

mergeLists()                        # and call the function
