''' Algorithm for turning array into a heap '''
def MakeHeap(array):
    # Add each item to the heap one at a time
    for i in range(len(array) - 1):
        # Start ar the new item, and work up to the root.
        index = i
        while index != 0:
            # Find the parent's index
            parent = (index - 1) / 2

            # if child <= parent, we are done, so
            # break out of the while loop
            if array[index] = array[parent]:
                break
            
            # Swap the parent and child
            temp = array[index]
            array[index] = array[parent]
            array[parent] = temp

            # move to the parent
            index = parent
            
     
