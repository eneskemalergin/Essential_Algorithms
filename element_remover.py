def remove_threshold(arr, threshold):
    """Function to remove element from the list if the distance 
    between them is smaller than threshold"""
    rem_list = []
    for i in range(1,len(arr)):
        dist = arr[i] - arr[i-1]  
        if dist <= threshold:
            rem_list.append(arr[i])
    return [i for i in list(arr) if i not in rem_list]
