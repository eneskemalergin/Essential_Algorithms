# Using Python
# This is for already defined 2 values
'''def GCD(a, b):
    while (b != 0):
        remainder = a % b
        a = b
        b = remainder
    return a
'''
# We are asking user to put input
a = input()
b = input()

# Returns the greatest common divisor of two numbers 
def GCD(a,b):
    while(b != 0):
        remainder = a % b
        a = b
        b = remainder
    return a

# Returns only two numbers least common multiplier
def LCM(a,b):
    return ((a * b) / GCD(a,b))


# Returns many different numbers' least common multiplier
def LCMM(*args):
    return reduce(GCDLCM, args)

print (GCD(a,b))
print (LCM(a,b))
