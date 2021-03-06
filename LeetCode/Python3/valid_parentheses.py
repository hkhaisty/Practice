class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        

class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
            
    def pop(self):
        if self.is_empty():
            return None
        
        data = self.top.data
        self.top = self.top.next
        
        return data
            
    def is_empty(self):
        return self.top is None


''' 
Solution -- Stack 
Runtime Complexity -- O(n) 
Space Complexity -- O(n) 
'''
def is_valid_parentheses(s):
    pairs = {'}':'{', ']':'[', ')':'('}
    chars = Stack()
    for c in s:
        if c not in pairs:
            chars.push(c)
        elif pairs[c] != chars.pop():
            return False
            
    return chars.is_empty()
