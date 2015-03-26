## Horner's Rule of Polynomial Evaluation
# Enes Kemal Ergin
# 03/26/15

""" 
coefficients := [-19, 7, -4, 6] # list coefficients of all x^0..x^n in order
when x = 3 
test HornerPolyEval()

Suggested Types: for coefficients use list of integers

"""
def HornerPolyEval(list_coeffs, x):
	result = 0
	for i in reversed(list_coeffs):
			result = result * x + i
	return result

# Test Case 1
# HornerPolyEval((-19,7,-4,6), 3)