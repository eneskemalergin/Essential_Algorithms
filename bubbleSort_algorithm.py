''' Bubble Sort Algorithm '''

def bubbleSort(theSeq):
    n = len(theSeq)
    # Perform n-1 bubble operations on the sequence
    for i in range(n-1):
        # Bubble the largest item to the end
        for j in range(i + n - 1):
            if theSeq[j-1] > theSeq[j ]: # Swap the j and j + 1 items
                temp =theSeq[j-1]
                theSeq[j-1] = theSeq[j]
                theSeq[j] = temp
        print theSeq        


bubbleSort([12, 5, 13, 8, 9, 65])
# Index Error: List index out of range
