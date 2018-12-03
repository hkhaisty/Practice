import unittest
from linked_list import LinkedList


def remove_duplicates(linked_list):
    nodes = {}
    previous = None
    current = linked_list.head
    while current is not None:
        if current.value in nodes:
            previous.next = current.next
        else:
            nodes[current.value] = current.value
            previous = current
        current = current.next


class Test(unittest.TestCase):
    values = [3, 3, 3, 1, 1, 2, 2, 1, 1, 2, 2, 3, 3]
    result = [3, 1, 2]

    def test_remove_duplicates(self):
        linked_list = LinkedList(None)
        for value in self.values:
            linked_list.append_to_tail(value)

        linked_list.head = linked_list.head.next
        remove_duplicates(linked_list)

        for value in self.result:
            self.assertEqual(value, linked_list.head.value)
            linked_list.head = linked_list.head.next


if __name__ == '__main__':
    unittest.main()
