import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def pop(self):
        data = self.head.data
        self.head = self.head.next

        return data

    def is_empty(self):
        return self.head is None


def triple_step(n):
    stack = Stack()
    stack.push(n)

    steps = [1, 2, 3]
    count = 0
    while not stack.is_empty():
        current = stack.pop()
        for step in steps:          
            diff = current - step
            if diff == 0:
                count += 1
            elif diff > 0:
                stack.push(diff)

    return count


class Test(unittest.TestCase):
    def test_triple_step(self):
        cases = [0, 1, 2, 3, 4, 5]
        expected = [0, 1, 2, 4, 6]

if __name__ == '__main__':
    unittest.main()
    