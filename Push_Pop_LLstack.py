# Pushing and Popping an item for linked list stack:

''' Those algorithms are working with already implemented linked list '''
def Push(sentinel, new_value):
    # Make a new cell to hold the new value
    new_cell = New_cell
    new_cell.value = new_value

    # Add the new cell to the linked list
    new_cell.next = sentinel.next
    sentinel.next = new_cell

def Pop(sentinel):
    if sentine.next == None:
        return "Already Empty"

    # Get the top cell's value
    result = sentinel.next.value

    # Remove the top cell from the linked list
    sentinel.next = sentinel.next.next

    return result


    
