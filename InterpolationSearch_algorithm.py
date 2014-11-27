''' Interpolation Search '''

def interpolationSearch(list, target):
    min = 0
    max = len(list) - 1
    while min <= max:
        # find the dividing item
        mid = min + (max - min) * (target - list[min])/(list[max]- list[min])

        if list[mid] == target:
            return mid
        
    
