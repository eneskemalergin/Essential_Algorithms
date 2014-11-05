# Showing pushing and popping items with two stacks contained in a single array

stack_values = [input()]

def Initialize():
    next_index1 = 0
    next_index2 = len(stack_values) - 1

    #End

    # Add an item to the top stack
def Push1(new_value):
    # Make sure there's room to add an item
    if(next_index1 > next_index2):
        return "Not Enough Room"
        
    # Add the new item,
    stack_values[next_index1] = new_value

    # Increment Next_index1
    next_index1 = next_index + 1

    # Add an item to the bottom stack
def Push2(new_value):
    # Make sure there's room to add an item.
    if next_index1 > next_index2:
        return "Not Enough Room"

    # Add the new item
    stack_values[next_index2] = new_value

    # Decrement next_index2
    next_index2 = next_index2 - 1

    # Remove an item from the top stack
def Pop1():
    # Make sure there's room to add an item
    if next_index1 == 0:
        return "Already Empty"

    # Decrement Next_index1
    next_index1 = next_index1 - 1

    # Return the top value
    return stack_values[next_index1]


    # Remove an item form the bottom stack
def Pop2():
    # Make sure there is an item to pop
    if next_index2 == len(stack_values) -  1:
        return "Already Empty"

    # Increment next_index2
    next_index2 = next_index2 + 1

    # Return the top value
    return stack_values[next_index2]
    
    





    
