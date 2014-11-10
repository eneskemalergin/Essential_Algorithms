# Stack Insertionsort #

''' Sort the items in the stack '''
''' For running this code we need stack data structure already implemented '''

# items and temp_stack are stack data type.
def StackInsertionsor(items):
    temp_stack = New Stack

    num_items = len(items)
    for i in range(num_items):
        # Position the next item
        # Pull off the first item
        next_item = items.Pop()

        # Implement following descriptions(guidance)
        ''' Move the items that have not yet been sorted to temp_stack.
            At this point there are (num_items - i - 1) unsorted items.>
        '''
        '''
            Move sorted items to the second stack until
            you find out where next_item belongs.
        '''
        ''' Add next_item at this position.'''
        ''' <Move the items back from temp_stack to the original stack.>'''
        
    # End
