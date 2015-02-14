# Randomizing Arrays
import random

def RandomizeArray(myList): # Needs to take list
    max_i = myList[len(myList) - 1] 
    print(myList)
    print(max_i)
    print(len(myList))
    i = 0
    for i in range(len(myList)):
        j = random.randint(i,(len(myList) - 1))
        temp = myList[i]
        myList[i] = myList[j]
        myList[j] = temp
    return myList  
# It is working
