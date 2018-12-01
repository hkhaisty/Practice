import unittest
from linked_list import LinkedList
from linked_list_node import LinkedListNode


def partition(linked_list, value):
    head = linked_list.root
    tail = linked_list.root
    while linked_list.root is not None:
        if linked_list.root.value < value:
            head.next = LinkedListNode(linked_list.root.value)
            head = head.next
        else:
            tail.next = LinkedListNode(linked_list.root.value)
            tail = tail.next
        linked_list.root = linked_list.root.next

    return left_partition


class Test(unittest.TestCase):
    values = [3, 5, 8, 5, 10, 2, 1]
    partition = 5
    expected = [3, 2, 1, 5, 8, 5, 10]

    def test_partition(self):
        linked_list = LinkedList(None)
        for value in self.values:
            linked_list.append_to_tail(value)
        linked_list.head = linked_list.head.next
        linked_list = partition(linked_list, self.partition)

        for value in self.expected:
            self.assertEqual(value, linked_list.root.value)
            linked_list.root = linked_list.root.next


if __name__ == '__main__':
    unittest.main()

