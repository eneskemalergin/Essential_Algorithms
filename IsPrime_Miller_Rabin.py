# This function is an imlementation of Miller-Rabin Primality Test.
"""
Miller-Rabin Primality test is the fastest algorithm so far for large n values.

This algorithm is accepting as a breakthrough in the study of probabilistic algorithms.
"""

import random
 
def decompose(n):
   exponentOfTwo = 0
 
   while n % 2 == 0:
      n = n/2
      exponentOfTwo += 1
 
   return exponentOfTwo, n
 
def isWitness(possibleWitness, p, exponent, remainder):
   possibleWitness = pow(possibleWitness, remainder, p)
 
   if possibleWitness == 1 or possibleWitness == p - 1:
      return False
 
   for _ in range(exponent):
      possibleWitness = pow(possibleWitness, 2, p)
 
      if possibleWitness == p - 1:
         return False
 
   return True
 
def probablyPrime(p, accuracy=100):
   if p == 2 or p == 3: return True
   if p < 2: return False
 
   numTries = 0
   exponent, remainder = decompose(p - 1)
 
   for _ in range(accuracy):
      possibleWitness = random.randint(2, p - 2)
      if isWitness(possibleWitness, p, exponent, remainder):
         return False
 
   return True