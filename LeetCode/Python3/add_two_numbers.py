class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


'''
Solution --
Runtime Complexity -- O(m + n)
Space Complexity -- O(max(m, n))
'''
def addTwoNumbers(self, l1, l2):
    current = lSum = ListNode(0)
    carry = 0
    while l1 or l2:
        l1_val = l1.val if l1 else 0
        l2_val = l2.val if l2 else 0
            
        add = l1_val + l2_val + carry
        carry = add // 10
        current.next = ListNode(add % 10)
    
        current = current.next
        l1 = l1.next if l1 else l1
        l2 = l2.next if l2 else l2
            
    if carry > 0:
        current.next = ListNode(carry)
            
    return lSum.next