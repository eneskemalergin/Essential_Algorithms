'''  Binary Search '''
def binarySearch(list, target):
    # Start with the entire sequence of elements
    low = 0
    high = len(list) - 1
    # We need to sort the list first
    list = list.sort()
    # Repeatedly subdivide the sequence in half until the target is found
    while low <= high:
        # find the midpoint of the sequence
        mid = (high+low) // 2
        # Does the midpoint contain the target?
        if list[mid] == target:
            return True
        # or does the target precede the midpoint?
        elif target < list[mid]:
            high  = mid - 1
        else:
            low = mid - 1
    return False


list = [12, 5, 13, 8, 9, 65]
print binarySearch(list, 9)        
    
# Something Wrong
