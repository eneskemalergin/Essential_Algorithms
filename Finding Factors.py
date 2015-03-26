def FindFactors(number):
    factors = []
    i = 2
    while (i < number):
        while(number % i == 0):
            factors.append(i)
            number = number / i
        i = i + 1
    if(number > 1):
        factors.append(number)
    return factors

print(FindFactors(1204))
