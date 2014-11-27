''' Counting Sort '''
def CountingSort(list, max_value):
    # Make and array to hold the counts
    counts = []

    # Initialize the array to hold the counts.
    for i in range(max_value):
        counts.append(0)

    # Count the items with each value
    for j in list:
        # Add 1 to the count for this value
        counts[j] += 1

    sortedList = []
    for i in range(max_value):
        if counts[i] > 0:
            for j in range(counts[i]):
                sortedList.append(i)
 
    return sortedList
print(CountingSort([2,16,77,65, 99, 4, 2, 16, 16], 100))
#expected [2,2,4,16,16,16,65,77,99]
