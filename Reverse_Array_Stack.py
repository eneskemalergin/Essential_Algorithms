# Reversing an Array using stack structure

def ReverseArray(values):
    # Push the values form the array onto the stack
    for i in values:
        stack.Push(values[i])


    # Pop the items off the stack into the array
    for i in values:
        values[i] = stack.Pop()

    
