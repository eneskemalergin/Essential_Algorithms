# Stack Selectionsort #

''' Sort the items in the stack '''

def StackSelectionsort(items):
    # Make the temporary stack
    temp_stack = New Stack

    num_items = len(Stack)
    for i in range(num_items):
        # Position the next item
        # Find the item that belongs in sorted position i

        '''Move the items that have not yet been sorted to temp_stack,
            keeping track of the largest. Store the largest item in variable
            largest_item.
            At this point there are (num_items - i - 1) unsorted items.'''

        '''Add largest_item to the original stack
            at the end of the previously sorted items.'''

        '''Move the unsorted items back from temp_stack to the
            original stack, skipping largest_item when you find it'''

    # End
    
