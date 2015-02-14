#Finding Prime Factors (Basic Version)

def FindFactors(number):
    my_list = []
    i = 2
    while(i <= number):
        while(number % i == 0):
            my_list.append(i)
            number = number / i
        i = i + 1

    # It adds any number left, it's also a factor    
    if (number > 1):
        my_list.append(number)
    return my_list
# It is Working
# I can remove the duplicatess from the list
