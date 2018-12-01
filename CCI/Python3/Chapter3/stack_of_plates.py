import unittest
from stack import Stack


class PlateStack(Stack):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        super().__init__()

    def push(self, data):
        self.size += 1
        super().push(data)

    def pop(self):
        self.size -= 1
        return super().pop()

    def size(self):
        return self.size

    def is_full(self):
        return self.size == self.capacity


class SetOfStacks:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stacks = []

    def get_current_stack(self):
        if len(self.stacks) == 0:
            return None

        return self.stacks[-1]

    def push(self, data):
        stack = self.get_current_stack()
        if stack is None or stack.is_full():
            stack = PlateStack(self.capacity)
            stack.push(data)
            self.stacks.append(stack)
        else:
            stack.push(data)

    def pop(self):
        stack = self.get_current_stack()
        if stack is None:
            raise Exception('Class: Set of Stacks is empty.')
        data = stack.pop()
        if stack.size == 0:
            self.stacks = self.stacks[:-1]

        return data


class Test(unittest.TestCase):
    values = [5, 7, 2, 3, 9, 9, 9, 9, 8, 7, 11, 3, 4]
    capacity = 5
    total_stacks = 3

    def test_set_of_stacks(self):
        set_of_stacks = SetOfStacks(self.capacity)
        for value in self.values:
            set_of_stacks.push(value)

        self.assertEqual(self.total_stacks, len(set_of_stacks.stacks))
        for value in self.values[::-1]:
            self.assertEqual(value, set_of_stacks.pop())


if __name__ == '__main__':
    unittest.main()

