'''
Solution - Hash Table
Runtime Complexity - O(n)
Space Complexity - O(n), n = unique characters in s
'''
def lengthOfLongestSubstring(self, s):
    char_idx = {}
    result = last_repeated = 0
    for i, c in enumerate(s), 1:
        if c in char_idx:
            last_repeated = max(last_repeated, char_idx[c])               
        char_idx[c] = i  
        result = max(result, i - last_repeated)
                
    return result
