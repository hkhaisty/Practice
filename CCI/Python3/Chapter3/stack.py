class Stack:
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = Stack.StackNode(None)

    def pop(self):
        if self.top is None:
            return None

        data = self.top.data
        self.top = self.top.next

        return data

    def push(self, data):
        node = Stack.StackNode(data)
        node.next = self.top
        self.top = node

    def peek(self):
        if self.top is None:
            return None

        return self.top.data

    def is_empty(self):
        return self.top is None
