'''
Solution - Hash Table
Runtime Complexity - O(n)
Space Complexity - O(n), n = unique characters in s
'''
class Solution:
    def length_of_longest_substring(self, s):
        char_idx = {}
        result = j = 0
        for i, c in enumerate(s):
            if c in char_idx:
                j = max(j, char_idx[c])               
            char_idx[c] = i + 1         
            result = max(result, i + 1 - j)
                
        return result
