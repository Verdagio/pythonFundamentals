
#Largest & smallest in a list

def opposites():
    list = []
    size = int(input("size of list?: "))

    for i in range(size):
        num = int(input("enter numnber: "))
        list.append(num)

    print("Max value: ", max(list), "\nMin value: ", min(list))

opposites()
