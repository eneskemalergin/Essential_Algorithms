
class Node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next
    def __str__(self):
        return(str(self.value))

    mynode1 = Node("1")
    mynode2 = Node("2")
    mynode3 = Node("3")

    mynode1.next = mynode2
    mynode2.next = mynode3

    def Iterate(top):
        while(top != None):
            print(top.Value)
            top = top.next
        # End While
    # End Iterate

    def FindCell(top, target):
        while(top != None):
            if(top.value == target):
                return (top)
            top = top.next
        # End While
        return None

    # End FindCell

    def FindCellBefore(top, target):
        if (top == None):
            return None
        # Search for the target Value
        while(top.next != None):
            if(top.next.Value2 == target):
                return (top)
            top = top.next
        # End While

        # If we get this far, the target is not in the list
        return None
    
    # End FindCellBefore

    # Modifiying the last code with usage of sentinel
    def FindCellBefore(top, target):
        # Search for the target value
        while(top.next != None):
            if (top.next.value == target):
                return (top)
            top = top.next
        # End While

        # If we get this far, the target is not in the list
        return None
    # End FindCellBefore

    '''
    Following algorithm adds a new item at the beginning of a linked list
    '''
    def AddAtBeginnig(top, new_cell):
        new_cell.next = top.next
        top.next = new_cell

    # End AddAtBeginning

    '''
    Following algorithm adds a new item at the end of a linked list
    '''
    def AddAtEnd(top, new_cell):
        # Find the last Cell.
        while(top.next != None):
            top = top.next
        # End wHile

        # Adds the new cell at the end
        top.next = new_cell
        new_cell.next = None
    # End AddAtEnd

    '''
    If we want to insert and item after specific cell
    '''

    def InsertCell(after_me, new_cell):
        new_cell.next = after_me.next
        after_me.next = new_cell
    #  End InsertCell


    '''
    Languages like java does not need to erase free cells
    they are using garbage collection system.
    If your language has something like garbage collection system
    use this function, otherwise next function will erase the free cells/
    '''
    def DeleteAfter(after_me):
        after_me.next = after_me.next.next
    # End DeleteAfter

    def DeleteAfter(after_me):
           target_cell = after_me.next
           after_me.next = after_me.next.next
           free(target_cell)#?
    # End DeleteAfter


    def DestroyList(top):
        while(top != None):
            # Save a Pointer to the next Cell
            next_cell = top.next

            # Free top.
            free(top) #?

            # move to the next cell
            top = next_cell
        # End While
    # End DestroyList
     

















































    

