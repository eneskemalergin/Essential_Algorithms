# Prints (gcd(), lastx, lasty)
def extendedGCD(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extendedGCD(b % a, a)
        return (g, x - (b // a) * y, y) # I didn't get it!

""" Print type: (gcd(a,b), x, y) """
print(extendedGCD(78, 42))


