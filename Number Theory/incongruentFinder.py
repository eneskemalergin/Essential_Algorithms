# Finding all incongruences for linear equations

def extendedGCD(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extendedGCD(b % a, a)
        return (g, x - (b // a) * y, y)

"""
From 6x is equivalent to 15 in mod 514
a  = 6
mod = 514
result = 15
"""

def incongrFind(a, mod, result):
	func = extendedGCD(a, mod)
	g = func[0]
	x = func[1]
	y = func[2]
	list_ = []
	
	#if gcd(a, mod) does not divide result
	if result % g != 0:
		# There is no solution 
		return list_
	
	x0 = x * (result/g)
	while g > 0:
		list_.append(x0)
		x0 = x0 + (g * ( mod / g))
		g -= 1

	return list_

# Test Cases	
print(incongrFind(42, 78, 12))
print(incongrFind(943, 2576, 381)) 
print(incongrFind(51, 1008, 177))
print(incongrFind(97, 53460, 1))
print(incongrFind(4, 19, 3))