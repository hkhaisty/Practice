class Stack:
    class StackNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.top = None

    def pop(self):
        if self.top is None:
            raise Exception('Empty Stack')

        data = self.top.data
        self.top = self.top.next

        return data

    def push(self, data):
        node = Stack.StackNode(data)
        node.next = self.top
        self.top = node

    def peek(self):
        if self.top is None:
            raise Exception('Empty Stack')

        return self.top.data

    def is_empty(self):
        return self.top is None
