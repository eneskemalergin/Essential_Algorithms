# Copied from internet, Author name is below:
__author__ = "Adam Traub"
__date__="2/16/2011"


class LinkedList:
    '''Linked List'''
    class __Node:
        '''
private node object.  Node's consist of an element
and a pointer to the previous and next Node'''
        def __init__(self, element=None):
            self.__element = element
            self.__next = None
            self.__previous = None
            self.__toMove = (self.getPrevious,self.getNext)

        def __str__(self):
            '''string representation of Node'''
            return str(self.__element)

        def hasNext(self):
            '''returns true if the Node has a next Node'''
            return self.__next != None

        def getNext(self):
            '''get next Node'''
            return self.__next

        def setNext(self,nextItem):
            '''set the next Node of the Node'''
            self.__next = nextItem
        
        def hasPrevious(self):
            '''returns true if the Node has a previous Node'''
            return self.__previous != None

        def getPrevious(self):
            '''get previous Node'''
            return self.__previous

        def setPrevious(self,previousItem):
            '''set the previous Node of the Node'''
            self.__previous = previousItem

        def getPreviousAndNext(self):
            '''gets previous and next Nodes'''
            return self.__previous,self.__next 

        def setPreviousAndNext(self, previousItem, nextItem):
            '''set the previous and Next Node of the Node'''
            self.__previous = previousItem
            self.__next = nextItem

        def getElement(self):
            '''get the element of the Node'''
            return self.__element           

        def setElement(self, element):
            '''set the element of the current Node'''
            self.__element = element

        def get(self,gettingNextElement):
            '''Get element based on a boolean.  True for next.  False for previous'''
            return self.__toMove[int(gettingNextElement)]()
            

    def __init__(self):
        '''Creates the LinkedList'''
        self.__first = LinkedList.__Node()
        self.__last = self.__first
        self.__length = 0

    def __len__(self):
        '''returns the length of the list O(1)'''
        return self.__length

    def count(self):
        '''returns the length of the list O(1)'''
        return self.__length

    def isEmpty(self):
        '''returns true if the list is empty'''
        return self.__length == 0

    def append(self, element):
        '''Add element to last position of the list'''
        self.__handleLinking(LinkedList.__Node(element),self.__last,None,False)
                    
    def pop(self, index =None):
        '''Removes and returns an element in the list. last element by default.'''
        if self.__length == 0:
            raise IndexError("pop from empty list")
        
        #utilize default parameter    
        if index ==None: 
            index = self.__length-1
        
        toRemove = self.__getNodeAtPosition(self.__checkIndex(index))        
        self.__handleLinking(toRemove,toRemove.getPrevious(),toRemove.getNext(),True)
        return toRemove.getElement()

    def insert(self, index, element):
        '''inserts an element to the given index'''
        toMove = self.__getNodeAtPosition(self.__checkIndex(index))
        self.__handleLinking(LinkedList.__Node(element),toMove.getPrevious(),toMove,False)

    def extend(self, toAdd):
        '''extend current list by adding an iterable structure to the end'''
        for value in toAdd:
            self.append(value)

    def index(self, x):
        '''Find index of first ocurrence of a given value'''
        for dex,value in enumerate(self):
            if x == value:
                return dex
        raise ValueError("LinkedList.index(x): x not in list")

    def reverse(self):
        '''reverse the linked list'''
        for index in range(self.__length-1,-1,-1):
            self.append(self.pop(index))

    def __getitem__(self, index):
        '''Allows for indexing, index must be an integer'''
        #accounts for slicing
        if type(index) == slice:
            return self.__sliceList(index)
        return self.__getNodeAtPosition(self.__checkIndex(index)).getElement()

    def __add__(self, other):
        '''adds a an iterable data structure to the linked list'''
        retList = LinkedList()
        for item in self:
            retList.append(item)
        for item in other:
            retList.append(item)
        return retList

    def __setitem__(self, index, element):
        '''Sets the item at a given index to a new element.'''
        self.__getNodeAtPosition(self.__checkIndex(index)).setElement(element)

    def __str__(self):
        '''returns a string representation of the list'''
        if self.__length == 0:    
            return '[]'
        retString = "["
        currentElement = self.__first.getNext()
        for i in range(self.__length):
            retString += str(currentElement) +", "
            currentElement = currentElement.getNext()
        
        return retString[:-2] + ']'


    #Private functions
    def __handleLinking(self, center, previous, nextNode, isRemoving):
        '''takes care of linking Nodes on inserts and removals'''
        def updateLinks(center, previous, nextNode, newNext, newLast, newPrevious, toAdd):
            '''A nested function to reduce repeated code in setting links'''
            if previous != None:
                previous.setNext(newNext)

            if nextNode == None:
                self.__last = newLast
            else:
                nextNode.setPrevious(newPrevious)
            self.__length += toAdd
            
            
        if isRemoving:
            updateLinks(center, previous, nextNode, nextNode, previous, previous, -1)
        else:
            center.setPreviousAndNext(previous,nextNode)
            updateLinks(center, previous, nextNode, center, center, center, 1)
            
                                
    def __sliceList(self,theSlice):
        '''(Private) function to handle slicing.  Returns a Linked List'''
        def determineStartStopStep(valToCheck, step, positiveStep, negativeStep):
            '''nested function to reduce repeated code in determining slicing handling'''
            if valToCheck == None:
                if step > 0:
                    return positiveStep
                else:
                    return negativeStep
            else:
                return valToCheck
            

        retList = LinkedList()        
        #Following conditions handles the x[start:stop:step] notation
        step  = determineStartStopStep(theSlice.step,1,1,1)
        start = determineStartStopStep(theSlice.start,step,0,self.__length-1)
        stop  = determineStartStopStep(theSlice.stop,step,self.__length,-1)

        currentNode = self.__getNodeAtPosition(start)
        gettingNext = step > 0
        absStep = abs(step)

        for eachItem in range(start,stop,step): 
            retList.append(currentNode)
            if eachItem + step <= stop:#prevents step from going out of bounds
                for i in range(absStep):
                    currentNode = currentNode.get(gettingNext)
        return retList

    
        
    def __getNodeAtPosition(self, index):
        '''(Private) Gets a Node at a given index'''
        movingForward = index < (self.__length//2)-1
        if movingForward:
            currentNode = self.__first
            toAdd = 1
        else:
            currentNode = self.__last
            index = (self.__length-1) - index
            toAdd = 0

        """
        Putting the for loop inside the condition would reduce the amount
        of times the conditon must be evaluated, increasing efficiency
        But would also simultaneously increase the amount of repeated code
        """
        for i in range(index+toAdd):
            currentNode = currentNode.get(movingForward)
        
        return currentNode

    def __checkIndex(self, index):
        '''(Private) check if the index is an acceptable value.  Index only changes if negative'''
        if type(index) != int:
            raise TypeError("Index must be an integer or a slice not a "+str(type(index)).split("'")[1])

        #handles negative indices.
        if index < 0:
            index += self.__length

        #If the index is out of bounds
        if index >= self.__length or index < 0:
            raise IndexError("Index out of bounds")
    
        return index
        
if __name__ == "__main__":
    import random
    def advanceWMessage(message):
        input(message+" press enter to continue")
    def printList(theList):
        print("Current List:"+str(theList))
        
    x = LinkedList()
    for i in range(30):
        x.append(i)
        
    printList(x)
    advanceWMessage("Testing slicing")
    for i in range(10):
        val1 = random.randint(0,len(x)//2)
        val2 = random.randint(len(x)//2,len(x))
        val3 = random.randint(1,len(x)//10)
        print("\n\nstart: "+str(val1))
        print("stop: "+str(val2))
        print("step: "+str(val3))
        print(x[val1:val2:val3])

    advanceWMessage("Insert -1 at beginning")
    x.insert(0,-1)
    printList(x)
        
        

