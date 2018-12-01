import unittest
from linked_list import LinkedList


def return_kth_element(linked_list, k):
    slow = fast = linked_list.root
    for i in range(k):
        if fast is None:
            return None
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow = slow.next

    return slow.value


class Test(unittest.TestCase):
    values = [5, 4, 3, 2, 1]

    def test_return_kth_element(self):
        linked_list = LinkedList(None)
        for value in self.values:
            linked_list.append_to_tail(value)
        linked_list.root = linked_list.root.next

        for i in range(len(self.values)):
            self.assertEqual(self.values[i], return_kth_element(linked_list, len(self.values) - i))


if __name__ == '__main__':
    unittest.main()

