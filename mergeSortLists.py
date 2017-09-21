
#merge & sort lists

def mergeLists():

    list1 = [1, 3, 5]
    list2 = [2, 4, 6]

    fList = list1 + list2

    print("Before: ", str(fList))

    list.sort(fList)

    print("after", str(fList))

mergeLists()
