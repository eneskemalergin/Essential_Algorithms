# Pushing and Popping an item for Array stack:

''' Those algorithms work only with already implemented Array structure '''

def Push(stack_values, next_index, new_value):
    # Make sure there's room to add an item

    if next_index == len(stack_values):
        return "Not Enough Space"

    # Add the new item
    stack_values(next_index) = new_value

    # Increment next_index
    next_index = next_index + 1

def Pop(stack_values, next_index):
    # Make sure there is na item to pop
    if next_index == 0 :
        return "Already Empty"

    # Decrement next_index
    next_index = next_index - 1

    # return the top value
    return stack_values(next_index)
