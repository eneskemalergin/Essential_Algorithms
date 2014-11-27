def countingsort(alist):
    counts = []
    for i in range(100):
        counts.append(0)
    for i in alist:
        counts[i] += 1
 
    sortedList = []
    for i in range(100):
        if counts[i] > 0:
            for j in range(counts[i]):
                sortedList.append(i)
 
    return sortedList
    

print(countingsort([2,16,77,65, 99, 4, 2, 16, 16]))
#expected [2,2,4,16,16,16,65,77,99]
