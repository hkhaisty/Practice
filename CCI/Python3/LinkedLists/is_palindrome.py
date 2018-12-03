import unittest
from linked_list import LinkedList
from linked_list_node import LinkedListNode


def is_palindrome(linked_list):
    reverse_list = LinkedList(None)
    current = linked_list.head
    while current is not None:
        head = reverse_list.head
        reverse_list.head = LinkedListNode(current.value)
        reverse_list.head.next = head
        current = current.next

    while reverse_list.head.value is not None:
        if reverse_list.head.value != linked_list.head.value:
            return False
        reverse_list.head = reverse_list.head.next
        linked_list.head = linked_list.head.next

    return True


class Test(unittest.TestCase):
    not_palindrome_values = [5, 6, 5, 0, 1, 1, 5]
    palindrome_values = [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    def test_is_palindrome(self):
        linked_list = LinkedList(None)
        for value in self.palindrome_values:
            linked_list.append_to_tail(value)
        linked_list.head = linked_list.head.next

        self.assertTrue(is_palindrome(linked_list))

    def test_not_palindrome(self):
        linked_list = LinkedList(None)
        for value in self.not_palindrome_values:
            linked_list.append_to_tail(value)
        linked_list.head = linked_list.head.next

        self.assertFalse(is_palindrome(linked_list))


if __name__ == '__main__':
    unittest.main()
