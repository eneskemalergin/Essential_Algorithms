# These functions work only with already defined node class.
#------------------------------------------------------------------------------#
#Question 1
'''
The section “Adding Cells at the End” gives an O(N) algorithm for adding
an item at the end of a singly linked list. If you keep another variable,
bottom, that points to the last cell in the list, you can add items to the end
of the list in O(1) time. Write such an algorithm. How does this complicate
other algorithms that add an item at the beginning or end of the list, fi nd
an item, and remove an item? Write an algorithm for removing an item
from this kind of list.
'''



def AddToEnd(first, new_cell):
    first.next = new_cell
    new_cell.Next = null
    
    return new_cell

def DeleteAfter(after_me, bottom):
    # If the cell being removed is the last one, update bottom
    if after_me.next == null :
        bottom = after_me

    # remove the target cell
    after_me.next = after_me.next.next

    # return a pointer to the last cell
    return bottom
#------------------------------------------------------------------------------#


# Question 2
'''
Write an algorithm to find the largest item in an unsorted singly linked
list with cells containing integers.
'''

def FindLargestCell(top):
    # If the list is empty return none
     if top.next == None:
         return None
    # Move to the first cell that holds data
    top = top.next

    # save this cell and its value
    best_cell = top
    best_value = best_cell.value

    # Move to the next cell
    top = top.next

    # Check the other cells
    while top != None:
        # See if this cell's value is bigger
        if top.value > best_value:
            best_cell = top
            best_value = top.value
        # Move to the next cell
        top = top.next


def findLargest(top):
    hold = top.value
    while top.next != None:
        if top < top.next:
            hold = top.next.value
        top = top.next
    return hold
#------------------------------------------------------------------------------#

# Question 3
'''
Write an algorithm to add an item at the top of a doubly linked list.
'''

def AddToTopDLL(top, new_cell):
    # Update the next links
    new_cell.next = top.next
    top.next = new_cell

    # Update the prev links
    new_cell.next.prev = new_cell
    new_cell.prev = top

#------------------------------------------------------------------------------#
    
# Question 4
'''
Write an algorithm to add an item at the bottom of a doubly linked list.
'''

def AddToBottom(bottom, new_cell):
    #Update the prev links
    new_cell.prev = bottom.prev
    bottom.prev = new_cell

    # Update the next links
    new_cell.prev.next = new_cell
    new_cell.next = bottom


#------------------------------------------------------------------------------#

# Question 5
'''
If you compare the algorithms you wrote for Exercises 3 and 4 to the
InsertCell algorithm shown in the section “Doubly Linked Lists,” you
should notice that they look very similar. Rewrite the algorithms you wrote
for Exercises 3 and 4 so that they call the InsertCell algorithm instead of
updating the list’s links directly.
'''

def AddToTop(top, new_cell):
    InsertCell(top, new_cell)

def AddToBottom(bottom, new_cell):
    InsertCell(bottom, new_cell)

#------------------------------------------------------------------------------#    

# Question 6
'''
Write an algorithm that deletes a specifi ed cell from a doubly linked list.
Draw a picture that shows the process graphically.
'''
        ''' Could not draw here '''
def DeleteCell(target):
    # Update the next cell's prev link
    target.next.prev = target.prev

    # Update the previous cell's next link
    target.prev.next = target.next
    
#------------------------------------------------------------------------------#
    
# Question 7
'''
Suppose you have a sorted doubly linked list holding names. Can you
think of a way to improve search performance by starting the search from
the bottom sentinel instead of the top sentinel? Does that change the Big
O run time?
'''

#------------------------------------------------------------------------------#
# Question 8
'''
Write an algorithm for inserting an item in a sorted doubly linked list
where the top and bottom sentinels hold the minimum and maximum
possible values.
'''
# Inserting a cell in a sorted doubly linked list
def InsertCell(top, new_cell):
    # Find the cell before where the new cell belongs
    while top.next.value < new_cell.value:
        top = rop.next

    # Update next links
    new_cell.next = top.next
    top.next = new_cell

    # Update the prev links
    # This part is special for DLL
    new_cell.next.prev = new_cell
    new_cell.prev = top
    
#------------------------------------------------------------------------------#
# Question 9
'''
Write an algorithm that determines whether a linked list is sorted.
'''
# Returns Boolean : True, False
def IsSorted(sentinel)
    # If the list has 0 or 1 element, it's sorted.
    if sentinel.next == None:
        return True
    elif sentine.next.next == None:
        return True

    # Compare the other items
    sentinel = sentinel.next
    while (sentinel.next !=  None):
        # Compare this item with the next one
        if sentine.value > sentinel.next.value:
            return False
        
        # Moves to next value
        sentinel = sentinel.next
    # If the loop finished and we get here, means list sorted.
    return True

#------------------------------------------------------------------------------#
# Question 10
'''
Insertionsort and selectionsort both have a run time of O(N2). Explain
why selectionsort takes longer in practice.
'''
#Insertionsort takes the fi rst item from the input list and then fi nds the place in the
#growing sorted list where that item belongs. Depending on its value, sometimes
#the item will belong near the beginning of the list, and sometimes it will belong
#near the end. The algorithm won’t always need to search the whole list, unless
#the new item is larger than all the items already on the sorted list.
#In contrast, when selectionsort searches the unsorted input list to fi nd the largest
#item, it must search the whole list. Unlike insertionsort, it can never stop the
#search early.

#------------------------------------------------------------------------------#


















    
