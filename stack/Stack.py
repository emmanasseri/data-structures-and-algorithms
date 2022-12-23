from Node import Node

class Stack:
    def __init__(self):
        self._elements = []

    def push(self, data):
        node = Node(data)
        self._elements.append(node)

    def pop(self):
        return self._elements.pop()

    def peek(self):
        return self._elements[-1]

    
