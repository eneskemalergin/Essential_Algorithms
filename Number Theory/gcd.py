# Great Common Divisor gcd(a,b)
# Author: Enes Kemal Ergin

""" Following method finds the great common divisor
for given numbers a and b  """
def gcd(a,b):
    while(b != 0):
        remainder = a % b
        a = b
        b = remainder
    return a

# Test Cases from Class
print gcd(60, 144)
print gcd(144, 60)
print gcd(335, 780)
print gcd(1160718174, 316258250)

# Test Cases from Book
print gcd(12345,67890)
print gcd(54321,9876)