import unittest
from stack import Stack


class StackWithMin(Stack):
    def __init__(self):
        super().__init__()
        self.stack = Stack()

    def push(self, data):
        if data <= self.min():
            self.stack.push(data)
        super().push(data)

    def pop(self):
        data = super().pop()
        if data == self.min():
            self.stack.pop()
        return data

    def min(self):
        if self.stack.is_empty():
            return float('Inf')

        return self.stack.peek()


class Test(unittest.TestCase):
    values = [5, 7, 3, 10, 2]
    min_values = [2, 3, 3, 5, 5]

    def test_stack_min(self):
        stack = StackWithMin()
        for value in self.values:
            stack.push(value)

        for value in self.min_values:
            self.assertEqual(value, stack.min())
            stack.pop()


if __name__ == '__main__':
    unittest.main()



