# Least Common Multiplier
# Author: Enes Kemal Ergin
from gcd import gcd
def lcm(a,b):
    return a * b / gcd(a,b)

# Test Cases
"""
print lcm(3,7)
print lcm(12,66)
print lcm(8,12)
print lcm(20,30)
print lcm(51,68)
print lcm(23,18)
"""