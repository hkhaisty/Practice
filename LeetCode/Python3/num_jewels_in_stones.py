'''
Solution -- Hash Set
Runtime Complexity -- O(J + S)
Space Complexity -- O(J)
'''
def num_jewels_in_stones(self, J, S):
    jewels = set(J)  
    num_jewels = 0
    for stone in S:
        if stone in jewels:
            num_jewels += 1
                
    return num_jewels

'''
Solution -- One Liner
Runtime Complexity -- O(J + S)
Space Complexity -- O(J + J ∩ S)
'''
def num_jewels_in_stones(self, J, S):
    return len([s for s in S if s in set(J)])
