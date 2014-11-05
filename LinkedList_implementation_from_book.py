# Lets implement a linked list
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

# Those are our objects or node
mynode1 = Node("first")
mynode2 = Node("Second")
mynode3 = Node("third")

# Now we can link them
mynode1.next = mynode2
mynode2.next = mynode3


#Printing the nodes after the node defined her as cell
#Iterate(mynode2)
#Result:
#Second
#third
def Iterate(cell):
    while (cell):
        print cell
        cell=cell.next

#Finding Nodes
#Cell: FindCell(Cell: top, Value: target)
def FindCell(top,target):

    #While (top != null)
    while (top != None):
        #If (top.Value == target) Then Return top
        if (top.value == target):
            return top
        #top = top.Next
        top = top.next
    return None

#print (FindCell(mynode2,"first"))

#Find Cell Before
#Cell: FindCellBefore(Cell: top, Value: target)
def FindCellBefore(top, target):
    if(top == None):
        return none
    while(top.next != None):
        if(top.next.value == target):
            return top
        top = top.next
    return None
#print FindCellBefore(mynode1, "first")

#add a sentinel to your links
sentinel = Node("")
sentinel.next = mynode1
'''
What is Sentinel?

    When we are looking for target value which is located in first node
    but we are looking at the target value's before value, it will throw an error.
    Sentinel prevents this situation to happen. Basically we are creating another
    object called sentinel before everthing, before actual linked list start.

'''
#-------------------------------------------------------------------#
#Adding cells at the beginning
#AddAtBeginning(Cell: top, Cell: new_cell)
def AddAtBeginning(top,new_cell):
#new_cell.Next = top.Next
    new_cell.next = top.next
#top.Next = new_cell
    top.next = new_cell
#End AddAtBeginning

new_one=Node("add me at the beginning")
AddAtBeginning(sentinel,new_one)
#Iterate(sentinel) #Beginning
#-------------------------------------------------------------------#
#Adding cells at the end
#AddAtEnd(Cell: top, Cell: new_cell)
def AddAtEnd(top,new_cell):
#// Find the last cell.
    #While (top.Next != null)
    while(top.next != None):
            #    top = top.Next
            top = top.next
    #// Add the new cell at the end.
    #top.Next = new_cell
    top.next = new_cell
    #new_cell.Next = null
    new_cell.next = None
#End AddAtEnd

new_one=Node("add me at the end")
AddAtEnd(sentinel,new_one)

#-------------------------------------------------------------------#
#Inserting after other cells
#InsertCell(Cell: after_me, Cell: new_cell)
def InsertCell(after_me,new_cell):
    #new_cell.Next = after_me.Next
    new_cell.next = after_me.next
    #after_me.Next = new_cell
    after_me.next = new_cell
#End InsertCell

new_one=Node("add me after SECOND")
InsertCell(mynode2,new_one)
#Iterate(sentinel)

#-------------------------------------------------------------------#

#Delete after me
#DeleteAfter(Cell: after_me)
def DeleteAfter(after_me):
    #after_me.Next = after_me.Next.Next
    after_me.next =after_me.next.next
#End DeleteAfter

#DeleteAfter(mynode2)
#Iterate(sentinel)
#-------------------------------------------------------------------#


#Destroy the List
#Pseudocode:
'''
DestroyList(Cell: top)
While (top != null)
// Save a pointer to the next cell.
Cell: next_cell = top.Next
// Free top.
free(top)
// Move to the next cell.
top = next_cell
End While
End DestroyList
'''


def DestroyList(top):
    while(top != None):
        # Save a pointer to the next cell
        next_cell = top.next
        
        #free(top) # In some languages you need to free the space
        # > but in python yo dont have to  
        # Move to the next cell
        top = next_cell














