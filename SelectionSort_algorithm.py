''' Selection Sort '''
def selectionSort(seq):
    n = len(seq)
    for i in range(n-1):
        # Assume the ith element is the smallest
        smallNdx = i
        # Determine if any other element contains smaller value
        for j in range(i + 1, n):
            if seq[j] < seq[smallNdx]:
                smallNdx = j

        # Swap the ith value and smallNdx value if the smallest value is
        # not already i ints proper position.
        if smallNdx != i:
            temp = seq[i]
            seq[i] = seq[smallNdx]
            seq[smallNdx] = temp
        print seq    
    return  seq        

selectionSort([12, 5, 13, 8, 9, 65])
