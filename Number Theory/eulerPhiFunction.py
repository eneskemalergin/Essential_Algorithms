def GCD(a, b):
    while (b != 0):
        remainder  = a % b
        a = b
        b = remainder
    return a  

def eulerPhiFun(m):
	M = [a for a in range(m+1) if 1 <= a <= m and GCD(a,m) == 1]
	print(M)
	print(len(M)) 

# eulerPhiFun(10) | 4 | ~ 0.0s
# eulerPhiFun(100) | 40 | ~ 0.0s
# eulerPhiFun(1000) | 400 | ~ 0.0s
# eulerPhiFun(10000) | 4000 | ~ 0.1s
# eulerPhiFun(100000) | 40000 | ~ 10.5s

#  Checks if Code is correct:
	#	to find GCD of random number from result with m
""" 
print(GCD(949, 1000))
print(GCD(351, 1000))
print(GCD(37, 1000))
print(GCD(13, 1000))

"""