#Finding Factors Fast
def FindingFactorsFast(number):
    factors = []

    while(number % 2 == 0):
        factors.append(2)
        number = number / 2

    i = 3
    max_factor = number ** 0.5 # sqrt(number)
    while(i <= max_factor):
        while(number % i == 0):
            factors.append(i)
            number = number / i
        
