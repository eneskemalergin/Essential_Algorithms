''' Implementation iof the queue using linked list '''
class LLQueue:
    def __init__(self):
        self._qhead = None
        self._qtail = None
        self._count = None

    def isEmpty(self):
        return self._qhead is None

    def __len__(self):
        return self._count

    def enqueue(self, item):
        node = _QueueNode(item)
        if self.isEmpty():
            self._qhead = None
        else:
            self._qtail = node

        self._qtail = node
        self._count += 1

    def dequeue(self):
        assert not self.isEmpty(), "Cannot dequeue from an empty queueu."
        node = self._qhead
        if self._qhead is self._qtail:
            self._qtail = None

        self._qhead = self.qhead.next
        self._count -= 1
        return node.item

class _QueueNode(object):
    def __init__(self, item):
        self.item = item
        self.cext = None
        
