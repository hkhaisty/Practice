import unittest
from stack import Stack


def sort(stack):
    temp = Stack()
    while not stack.is_empty():
        data = stack.pop()
        while not temp.is_empty() and temp.peek() > data:
            stack.push(temp.pop())
        temp.push(data)

    while not temp.is_empty():
        stack.push(temp.pop())


class Test(unittest.TestCase):
    values = [12, 8, 10, 1, 3, 7]
    expected = [1, 3, 7, 8, 10, 12]

    def test_sort(self):
        stack = Stack()
        for value in self.values:
            stack.push(value)
        sort(stack)

        for value in self.expected:
            self.assertEqual(value, stack.pop())


if __name__ == '__main__':
    unittest.main()



