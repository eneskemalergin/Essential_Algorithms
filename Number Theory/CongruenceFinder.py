# Brute-force congruence Finder
# Author: Enes Kemal Ergin
"""
ax = b(mod -mod-)
	a is a integer constant
	b is a integer remainder
	x is a result that we want to obtain
	-mod- is a integer which base we want to find x

	This is the least efficient method: 
"""
# ax = b type
def congrFindV1(a, mod = 10, result = 0):
	p=[]
	for x in range(0,mod):               
	   if (a*x) % mod == result :
	      p.append(x)           
	return p



import time # To check the execution time

# Test Cases solved in Class
start_time = time.time() # To check the execution time
print(congrFindV1(18,22, 8))
print("1st Execution: %.5s miliseconds" % (time.time() - start_time))# To check the execution time

start_time = time.time()
print(congrFindV1(4,19, 3))
print("2nd Execution: %.5s miliseconds" % (time.time() - start_time))# To check the execution time

start_time = time.time() # To check the execution time
print(congrFindV1(6, 514, 15))
# No Result because divisibilty error.
print("3rd Execution: %.5s miliseconds" % (time.time() - start_time))# To check the execution time
