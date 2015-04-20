# Author: Enes Kemal Ergin
# 03/27/15
# This is the fastest implementation so far
def largest_prime(number):
	largest_prime = 0
	counter = 2
	while counter * counter <= number:
		if number % counter == 0:
			number = number / counter
			largest_prime = counter
		else:
			counter += 1
	if number > largest_prime:
		largest_prime = number
	print largest_prime

largest_prime(52633)