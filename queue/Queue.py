# A Queue operates by FIFO
# meaning the first element in is the first element taken out
# for a stack, a variable is set to track the newest node added
# for a queue, a variable is set to track the oldest node added
from Node import Node

class Queue:
    def __init__(self):
        self._front = None
        self._back = None
        self._isEmpty = True

    def enqueue(self, data):
        node = Node(data)
        if(self._isEmpty == True):
            self._front = node
        self._back = node
        self._isEmpty = False

    def peekFront(self):
        return self._front

    

        

