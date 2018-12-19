'''
Solution -- Working Backwards
Runtime Complexity -- O(n), n = len(S)
Space Complexity -- O(n)
'''
def license_key_formatting(self, S, K):
    chars = []
    count = 0
    for i in range(len(S) - 1, -1, -1):
        if S[i] == '-':
            continue
            
        if count == K:
            chars.append('-')  
            count = 0
                
        chars.append(S[i].upper())
        count += 1

                
    return ''.join(chars[::-1])
            

'''
Solution -- Using Substrings and Replace
Runtime Complexity -- O(n)
Space Complexity -- O(n)
'''
def license_key_formatting(self, S, K):
    S = S.replace('-', '').upper()
        
    substrings = []
    if len(S) % K > 0:
        substrings.append(S[:len(S) % K])
    for i in range(len(S) % K, len(S), K):
        substrings.append(S[i:i+K])
        
    return '-'.join(substrings)