import math
# newtons method for square roots

x = 20
z = 1
z_next = (z - ((z * z - x) / (2 * z)))


while z != z_next(z):
    print("current guess %0,10f\tnext guess: %0.10f", (z, z_next(z)))
    z = (z_next(z))

