import unittest
from linked_list import LinkedList


def sum_lists(list_1, list_2):
    result = LinkedList(None)
    carry = 0
    while list_1.head is not None and list_2.head is not None:
        if list_1.head is None:
            value = list_2.head.value + carry
        elif list_2.head is None:
            value = list_1.head.value + carry
        else:
            value = list_1.head.value + list_2.head.value + carry

        carry = value // 10
        result.append_to_tail(value % 10)
        list_1.head = list_1.head.next
        list_2.head = list_2.head.next

    result.head = result.head.next
    return result


def sum_lists_forward(list_1, list_2):
    result = LinkedList(None)
    prev = result.head
    carry = 0
    while list_1.head is not None and list_2.head is not None:
        if list_1.head is None:
            value = list_2.head.value
        elif list_2.head is None:
            value = list_1.head.value
        else:
            value = list_1.head.value + list_2.head.value

        result.append_to_tail(value % 10)
        carry = value // 10
        if prev.value is None:
            prev = prev.next
        else:
            prev.value += carry
            prev = prev.next
        list_1.head = list_1.head.next
        list_2.head = list_2.head.next

    result.head = result.head.next
    return result


class Test(unittest.TestCase):
    list1_values = [7, 1, 6]
    list2_values = [5, 9, 2]
    expected = [2, 1, 9]

    def test_sum_lists(self):
        list_1 = LinkedList(None)
        for value in self.list1_values:
            list_1.append_to_tail(value)
        list_1.head = list_1.head.next

        list_2 = LinkedList(None)
        for value in self.list2_values:
            list_2.append_to_tail(value)
        list_2.head = list_2.head.next

        result = sum_lists(list_1, list_2)
        for value in self.expected:
            self.assertEqual(value, result.head.value)
            result.head = result.head.next

    def test_sum_lists_forward(self):
        list_1 = LinkedList(None)
        for value in self.list1_values[::-1]:
            list_1.append_to_tail(value)
        list_1.head = list_1.head.next

        list_2 = LinkedList(None)
        for value in self.list2_values[::-1]:
            list_2.append_to_tail(value)
        list_2.head = list_2.head.next

        result = sum_lists_forward(list_1, list_2)
        for value in self.expected[::-1]:
            self.assertEqual(value, result.head.value)
            result.head = result.head.next


if __name__ == '__main__':
    unittest.main()



