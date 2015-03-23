# Section 1 ~ Series

# Question 1
""" Find the sum of the series 1 + 1/2 + 1/3 + 1/4 + .... + 1/100 """

def Q1(upper = 100):
	sum = 0
	for i in range(1,upper+1):
		sum = sum + 1/i
	return(sum)
# Question 2
""" Find the sum 1 + 1/2^2 + 1/3^2 + .... + 1/100^2 """

def Q2(upper = 100):
	sum = 0
	for i in range(1, upper+1):
		sum += 1/(i**2)
	return(sum)
# Question 3
""" Find the sum 1 - 1/2 + 1/3 - 1/4 + .... + 1/99 - 1/100 """

def Q3(upper = 100):
	sum = 0 
	k = 1
	while k <= 100:
		if k % 2 == 1:
			sum += 1/k
		else:
			sum -= 1/k
		k += 1
	return(sum)

# Question 4
""" Define a function factorial(n) that computes n! = 1.2.3...n"""
def factorial(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return (n * factorial(n-1) )

# Question 5
""" Define a binomial to compute binomial coefficients. """

def log_binomial(n,k): 
	return (log_fac(n)-log_fac(k)-log_fac(n-k))


