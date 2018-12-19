'''
Solution -- Hash Table 
Runtime Complexity -- O(n)
Space Complexity -- O(n)
'''
def two_sum(nums, target):
    complements = {}
    for i, n in enumerate(nums):
        if n in complements:
            return [complements[n], i]

        complements[target - n] = i

    return None
