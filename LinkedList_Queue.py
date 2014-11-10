# Linked-List Queues #

def Enqueue(top_sentinel, new_value):
    # Make a cell to hold the new value
    new_cell = New Cell
    new_cell.value = new_value

    # Add the new cell to the linked list
    new_cell.next = top_sentinel.next
    top_sentinel.next = new_cell
    new_cell.prev = top_sentinel

    
def Dequeue(bottom_sentinel):
    # Make sure there is an item to dequeue
    if (bottom_sentinel.prev == top.sentinel):
        return "Already Empty"
    else:
        # Get the bottom cell's value
        result = bottom_sentinel.prev.value

        # Remove the bottom cell from the linked list
        bottom_sentinel.prev = bottom_sentinel.prev.prev
        bottom_sentinel.prev.next = bottom_sentinel

        # Returns the result
        return result
