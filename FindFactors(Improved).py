#Finding Factors(Improved Algorithm)
import math
def FindFactors(number):
    factors = []
    while(number % 2 == 0):
        factors.append(2)
        number = number / 2
    #End While

    #Looking for Odd factors
    i = 3
    max_factor = math.sqrt(number)
    while(i <= max_factor):
        while((number % i) == 0):
            # i is a factor add the list 
            factors.append(i)

            # divide the number by i
            number = number / i

            # set a new upper bond

            max_factpr = math.sqrt(number)
        # End While

        # Checks next ODD number
        i = i + 2

    # End While

    if (number > 1):
        factors.append(number)
    return factors
