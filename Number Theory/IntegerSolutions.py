# 
# Author: Enes Kemal Ergin

"""
Find positive integer solutions to the equation x^2 - 2y^2 = 1
	Parameters:
		n -> Find solutions until n
"""

def psearch(n):
	for x in range(0, n):
		for y in range(0, n):
			if x*x - 2*y*y == 1:
				print x, y 


# Tests
psearch(1000)


