# This function checks the number if it is prime or not...
# Author : Enes Kemal Ergin
# Date   : 02/14/15
# Return true if the number p is prime...
import random
def IsPrime(p, max_tests):
    # Perform the test up to max_tests times
    for i in range(max_tests):
        n = random.randint(1, p - 1)
        if (pow(n, p-1) % p) != 1:
            return False
    
    # If the loop finish executing and did not return False we got probably a prime.
    # There is pow(1/2,max_test) chance that it is not prime.
    return True

## Tests
IsPrime(2,1)
IsPrime(3,1)
IsPrime(15,10)
IsPrime(19,10)