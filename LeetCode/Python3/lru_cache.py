class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, node):
        if self.tail is not None:
            node.prev = self.tail
            node.next = self.head
            self.tail.next = node
        self.tail = node

        if self.head is None:
            self.head = self.tail

    def pop(self):
        if self.is_empty():
            return None

        node = self.head
        self.remove(node)
        if self.head is None:
            self.tail = None

        return node

    def remove(self, node):
        if node == self.head:
            self.head = node.next
            if self.head is None:
                self.tail = None
        elif node == self.tail:
            self.tail = node.prev
            if self.tail is None:
                self.head is None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
          
    def is_empty(self):
        return self.head is None
    

'''
Solution -- Hash Table and Doubly Linked List 
Runtime Complexity -- O(1) 
Space Complexity -- O(capacity)
'''
class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.nodes = DoublyLinkedList()
              
    def get(self, key):
        if key in self.cache:
            self.replace(key, self.cache[key].value)
            return self.cache[key].value
        
        return -1

    def put(self, key, value):
        if key not in self.cache:
            if len(self.cache) == self.capacity:
                del self.cache[self.nodes.pop().key]

            node = Node(key, value)
            self.nodes.push(node)
            self.cache[key] = self.nodes.tail
        else:
            self.replace(key, value)
            
    def replace(self, key, value):
        node = self.cache[key]
        self.nodes.remove(node)
        self.nodes.push(node)
        node.value = value