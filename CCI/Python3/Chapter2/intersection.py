import unittest
from linked_list import LinkedList
from linked_list_node import LinkedListNode


def get_tail_and_size(head):
    size = 1
    while head.next is not None:
        size += 1
        head = head.next

    return head.value, size


def intersection(list_1, list_2):
    if list_1.head is None or list_2.head is None:
        return None

    l1_tail, l1_size = get_tail_and_size(list_1.head)
    l2_tail, l2_size = get_tail_and_size(list_2.head)

    if l1_tail != l2_tail:
        return None

    shorter = list_1.head if l1_size <= l2_size else list_2.head
    longer = list_1.head if l1_size > l2_size else list_2.head

    for i in range(abs(l1_size - l2_size)):
        longer = longer.next

    while shorter.value != longer.value:
        shorter = shorter.next
        longer = longer.next

    return shorter.value


class Test(unittest.TestCase):
    l1_values = [3, 1, 5, 9, 7, 2, 1]
    l2_values = [4, 6, 7, 2, 1]
    expected = 7

    def test_intersection(self):
        list_1 = LinkedList(None)
        for value in self.l1_values:
            list_1.append_to_tail(value)
        list_1.head = list_1.head.next

        list_2 = LinkedList(None)
        for value in self.l2_values:
            list_2.append_to_tail(value)
        list_2.head = list_2.head.next

        self.assertEqual(self.expected, intersection(list_1, list_2))



if __name__ == '__main__':
    unittest.main()