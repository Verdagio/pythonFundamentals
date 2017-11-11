import math                       # import the maths module
# newtons method for square roots

x = 20 
z = 1
z_next = (z - ((z * z - x) / (2 * z)))   # maths....  see: https://en.wikipedia.org/wiki/Newton%27s_method


while z != z_next(z):                    # loop while z is not = z_next * z
    print("current guess %0,10f\tnext guess: %0.10f", (z, z_next(z)))   #print out both values
    z = (z_next(z))                       # set the current z to the next so that we don't get stuck in a pointless endless loop.

