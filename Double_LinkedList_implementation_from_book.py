# Implementatation of basic Double Linked List

# Improvement of Double Linked list is:
# You can search delete or reach from backwards.
class Node:
    def __init__(self, value=None, next=None, prev=None):
        self.value = value
        self.next  = next
        self.prev = prev  # prev allows you to go back.

    def __str__(self):
        return str(self.value)


def ShowPrevNext(node):
    print node.prev,"<--", node , "-->",node.next

#Create nodes
mynode1= Node("first")
mynode2= Node("second")
mynode3= Node("third")

#link them
mynode1.next = mynode2
mynode2.next = mynode3

mynode2.prev = mynode1
mynode3.prev = mynode2

ShowPrevNext(mynode2) # Shows next and prev node of it.

def InsertCell(after_me, new_cell):
    #Update Next Links
    new_cell.next = after_me.next
    after_me.next = new_cell

    #Update prev links
    new_cell.next.prev = new_cell
    new_cell.prev = after_me
    

new_node= Node("new one")
InsertCell(mynode2, new_node)
