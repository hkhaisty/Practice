import unittest
from linked_list import LinkedList


def delete_middle_node(middle_node):
    if middle_node is None or middle_node.next is None:
        return None

    middle_node.value = middle_node.next.value
    middle_node.next = middle_node.next.next


class Test(unittest.TestCase):
    values = [1, 2, 3, 4, 5, 6]
    middle_node_value = 3
    expected = [1, 2, 4, 5, 6]

    def test_delete_middle_node(self):
        linked_list = LinkedList(None)
        for value in self.values:
            linked_list.append_to_tail(value)
        linked_list.head = linked_list.head.next

        middle_node = linked_list.head
        while middle_node.value != self.middle_node_value:
            middle_node = middle_node.next
        delete_middle_node(middle_node)

        for value in self.expected:
            self.assertEqual(value, linked_list.head.value)
            linked_list.head = linked_list.head.next


if __name__ == '__main__':
    unittest.main()



