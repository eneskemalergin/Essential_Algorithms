a = 876
b = 1587
def GCD(a, b):
    while (b != 0):
        remainder  = a % b
        a = b
        b = remainder
    return a    
