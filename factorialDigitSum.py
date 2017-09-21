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

print("Factorial sum of 100 Result: ", res)