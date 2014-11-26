''' Insertion Sort '''
def insertionSort(seq):
    n = len(seq)
    # Starts with the first item as the only sorted entry
    for i in range(1, n):
        # save the value to be positioned
        value = seq[i]
        # Find the position where value fits in the ordered part of the list
        pos = i
        while pos > 0 and value < seq[pos - 1]:
            # shift the items to the right during the search
            seq[pos] = seq[pos - 1]
            pos -= 1
        seq[pos] = value
        print seq
    return seq

insertionSort([12, 5, 13, 8, 9, 65])
