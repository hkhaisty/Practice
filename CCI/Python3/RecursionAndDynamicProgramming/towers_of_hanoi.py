import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def pop(self):
        data = self.head.data
        self.head = self.head.next
        self.size -= 1

        return data

    def peek(self):
        return self.head.data
        
    def is_empty(self):
        return not self.head


class Tower:
    def __init__(self):
        self.disks = Stack()

    def add(self, disk):
        if self.disks.is_empty() or self.disks.peek() > disk:
            self.disks.push(disk)

    def move_top(self, tower):
        tower.add(self.disks.pop())

    def move_disks(self, n, destination, buffer):
        if n > 0:
            self.move_disks(n - 1, buffer, destination)
            self.move_top(destination)
            buffer.move_disks(n - 1, destination, self)

    def equals(self, tower):
        if self.disks.size != tower.disks.size:
            return False

        sHead = self.disks.head 
        tHead = tower.disks.head
        while sHead and tHead:
            if sHead.data != tHead.data:
                return False
            sHead = sHead.next
            tHead = tHead.next

        return True


def towers_of_hanoi(n):
    t1 = t2 = t3 = Tower()
    for i in range(n, 0, -1):
        t1.add(i)
    t1.move_disks(n, t2, t3)

    return t3


class Test(unittest.TestCase):
    def test_towers_of_hanoi(self):
        cases = [0, 1, 2, 3, 4, 5]
        towers = [Tower() for n in range(6)]
        for i in range(len(towers)):
            for j in range(i, 0, -1):
                towers[i].add(j)

        for tower, case in zip(towers, cases):
            self.assertTrue(tower.equals(towers_of_hanoi(case)))


if __name__ == '__main__':
    unittest.main()
