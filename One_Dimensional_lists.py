# One Dimensional Arrays(Lists in Python):
''' In Python there is no specific data structures called arrays '''
'''             We are using lists instead of arrays             '''


''' Finding Items in List   '''
def IndexOf(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    # Returns False means target not in the list
    return False
    #   O(N) Efficiency

''' Finding Minimum value in the list   '''
def FindMin(list):
    minimum = list[0]
    for i in list:
        if list[i] < minimum:
            minimum = list[i]

    return minimum

''' Finding Maximum value in the list   '''

def FindMax(list):
    maximum  = list[0]
    for i in list:
        if list[i] > maximum:
            maximum = list[i]

    return maximum

''' Finding Average of the list     '''
def FindAverage(list):
    total = 0
    for i in list:
        total += list[i]

    return total / len(list)


''' Finding the median of the List '''
def FindMedian(list):
    for i in list:
        # Finding the number of values greater than and less than array[i]
        num_smaller = 0
        num_greater = 0

        for j in list:
            if(list[j] < list[i]):
                num_smaller += 1
            elif(list[j] > list[i]):
                num_greater += 1
            else:
                pass

        if num_smaller == num_greater:
            return list[i]
    # O(NxN) Efficiency


''' Inserting an element to the end of the list     '''
def InsertToEnd(list):
    # Taking value from the user
    value = raw_input()
    # Appending to the end of the list
    list.append(value)

    ''' Copying the list to another using append:   '''
    
    ar = []  # Make an empty list
    for i in list:
        ar.append(i)

    print ar

    return None


    
def InsertToIndex(list):
    # Taking value from the user
    value = raw_input()
    # Ask user for index
    index = raw_input()
    # Add value to specific index
    list.insert(index, value)



    




































    
