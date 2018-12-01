from linked_list_node import LinkedListNode


class LinkedList:
    def __init__(self, value):
        self.head = LinkedListNode(value)

    def append_to_tail(self, node_value):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = LinkedListNode(node_value)

    def delete_node(self, node_value):
        current = self.head
        while current.next is not None:
            if current.next.value == node_value:
                current.next = current.next.next
                break
            current = current.next

    def pop_node(self, node_value):
        current = self.head
        while current.next is not None:
            if current.next.value == node_value:
                node = current.next
                current.next = current.next.next
                return node

        return None


