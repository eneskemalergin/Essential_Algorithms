# Inserting an item into a sorted singly linked list:

'''
        This is very useful to add item to list in position that it needs to be in
'''
def InsertCell(top, new_cell):
    #Find the cell before where the new cell belongs
    while (top.next != None) and (top.next.value < new_cell.value):
        top = top.next
    #insert The cell after top

    new_cell.next = top.next
    top.next = new_cell

# following function do the same as the one above with sentinel;    
def InsertCellWithSentinel(top, new_cell):
    #Find the cell before where the new cell belongs
    while(top.next.value < new_cell.value):
        top = top.next

    # Insert the new cell after top
    new_cell.next = top.next
    top.next = new_cell
    
