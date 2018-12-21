'''
Solution --
Runtime Complexity -- O(n)
Space Complexity -- O(1)
'''
def maximum_subarray(self, nums):
    currSum = maxSum = -float('Inf')
    for n in nums:
        if currSum < 0 and n > currSum:
            currSum = n
        else:
            currSum += n
        maxSum = max(maxSum, currSum)
            
    return maxSum
                