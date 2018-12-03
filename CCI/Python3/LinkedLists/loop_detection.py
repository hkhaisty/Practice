import unittest
from linked_list import LinkedList
from linked_list_node import LinkedListNode


def loop_detection(linked_list):
    nodes = {}
    while linked_list.head is not None:
        if linked_list.head in nodes:
            return linked_list.head.value
        else:
            nodes[linked_list.head] = linked_list.head.value

        linked_list.head = linked_list.head.next

    return None


def loop_detection_no_extra_space(linked_list):
    slow = fast = linked_list.head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    if fast is None or slow is None:
        return None

    slow = linked_list.head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast.value


class Test(unittest.TestCase):
    loop_values = ['A', 'B', 'D', 'E']
    expected = 'C'

    def test_loop_detection(self):
        loop_list = LinkedList(None)
        for value in self.loop_values:
            loop_list.append_to_tail(value)
        loop_list.head = loop_list.head.next

        node = LinkedListNode('C')
        current = loop_list.head
        while current.value != 'B':
            current = current.next
        node.next = current.next.next
        current.next = node

        while current.next is not None:
            current = current.next
        current.next = node

        self.assertEqual(self.expected, loop_detection(loop_list))
        self.assertEqual(self.expected, loop_detection_no_extra_space(loop_list))


if __name__ == '__main__':
    unittest.main()
