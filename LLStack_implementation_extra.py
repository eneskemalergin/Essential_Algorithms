''' Implementation of stack using a singly linked list '''
class LLStack:
    # Creates an empty stack
    def __init__(self):
        self._top = None
        self._size = 0

    # Returns True if the stack is empty
    def isEmpty(self):
        return self._top is None

    # Return the top item on the stack without removing it
    def peek(self):
        assert not self.isEmpty(), "Cannot peek at an empty stack"
        return self._top.item

    # Removes and returns the top item on the stack
    def pop(self):
        assert not self.isEmpty(), "Cannot pop from an empty stack"
        node = self._top
        self.top = self._top.next
        self._size -= 1
        return node.item

    # Pushes and item onto the top of the stack
    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size += 1
# Private storage class for creating stack nodes
class _StackNode:
    def __init__(self, item, link):
        self.item = item
        self.next = link
        
