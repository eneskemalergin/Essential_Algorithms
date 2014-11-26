''' Implementing a Queue using Python List '''
class Queue:
    #Creates an empty queue
    def __init__(self):
        self._qlist = list()

    # Returns True if the queue is empty
    def isEmpty(self):
        return len(self) == 0

    # Returns the number of items in the queue
    def __len__(self):
        return len(self._qlist)

    # Adds the given item to the queue
    def enqueue(self, item):
        self._qlist.append(item)
    # Removes and returns the first item in the queue
    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from and empty queue."
        return self._qlist.pop(0)
