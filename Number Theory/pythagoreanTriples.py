# Author: Enes Kemal Ergin
#03/26/15

"""
Primordial Algortihm to find Pythagorean Triples using

a^2 + b^2 = c^2 equations to find PT's

PT() function requires 1 parameter n which is the upper limit of
c in PT. When looping reach that point looping stops.
"""
def PT(n):
	counter = 1
	for a in range(1,n):
		for b in range(a, n):
			for c in range(b,n):
				if a**2 + b**2 == c**2:
					print(str(counter) + ')', a, b, c)
					counter += 1 	
	return n		
# Test Case
# print(PT(100))
"""
This is more advanced method of finding Primitive Pythagorean Triples


"""

from math import sqrt
def PPT(n):                                                 
    a, b, c = 1, 3, 0                                                       
    while c < n:                                                            
        a_ = (a * b) + a                                                    
        c = sqrt(a_**2 + b**2)                                         
        if c == int(c):                                                     
            yield b, a_, int(c)                                             
        a += 1                                                              
        b += 2

# Test Case
for pt in pythagorean_triples(1000):                        
    print(pt)