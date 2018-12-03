class MyQueue:
    class QueueNode:
        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.first = MyQueue.QueueNode(None)
        self.last = MyQueue.QueueNode(None)

    def add(self, data):
        node = MyQueue.QueueNode(data)
        if self.last is not None:
            self.last.next = node
        self.last = node

        if self.first is None:
            self.first = self.last

    def remove(self):
        if self.first is None:
            return None

        data = self.first.data
        self.first = self.first.next
        if self.first is None:
            self.last = None

        return data

    def peek(self):
        if self.first is None:
            return None

        return self.first.data

    def is_empty(self):
        return self.first is None
