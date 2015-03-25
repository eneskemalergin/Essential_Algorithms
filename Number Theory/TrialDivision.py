# Trial Division
# Author: Enes Kemal Ergin

"""
Factorizations slowest to fastest
"""
def factor1(n):
	d = 2
	while n>1:
		if n%d == 0:
			n = n/d
			print d,
		else:
			d += 1
	print
	return n

# Tests 
factor1(1234)

factor1(4321)