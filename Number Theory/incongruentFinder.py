# Finding all incongruences

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
# There is a bug to fix
def incongrFind(a, mod, result):
	func = extendedGCD(a, mod)
	g = func[0]
	x = func[1]
	y = func[2]
	list_ = []
	if (result/g) != int:
		return list_
	if g != result:
		x0 = result / g
	
	while g > 0:
		list_.append(x0)
		x0 = x0 + g * (mod/g)
		g -= 1

	return list_
print(incongrFind(42, 78, 12))
print(incongrFind(943, 2576, 381)) # Supposed to be No solutions
