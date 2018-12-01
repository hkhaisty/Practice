import unittest
from linked_list import LinkedList


def partition(linked_list, value):
    head = tail = current = linked_list.head
    while current is not None:
        next_node = current.next
        if current.value < value:
            current.next = head
            head = current
        else:
            tail.next = current
            tail = tail.next
        current = next_node

    return head


class Test(unittest.TestCase):
    values = [3, 5, 8, 5, 10, 2, 1]
    partition = 5
    expected = [1, 2, 3, 5, 8, 5, 10]

    def test_partition(self):
        linked_list = LinkedList(None)
        for value in self.values:
            linked_list.append_to_tail(value)
        linked_list.head = linked_list.head.next
        linked_list.head = partition(linked_list, self.partition)

        for value in self.expected:
            self.assertEqual(value, linked_list.head.value)
            linked_list.head = linked_list.head.next


if __name__ == '__main__':
    unittest.main()

