import unittest


def is_permutation_of_palindrome(string):
    if not string:
        return False

    chars = {}
    oddCount = 0
    for char in string:
        if char == ' ':
            continue
        
        if char not in chars:
            chars[char] = 0

        chars[char] += 1
        oddCount += 1 if chars[char] % 2 != 0 else -1
    
    return oddCount <= 1


class Test(unittest.TestCase):
    permutations = ['atco cta', 'tact coa', 'coat cat', 'cota toa', 'cat taco']
    not_permutations = ['atco cca', 'accooo at', 'catto tac', '', 'taco cac']

    def test_permutations(self):
        for permutation in self.permutations:
            self.assertTrue(is_permutation_of_palindrome(permutation))
        
    def test_not_permutations(self):
        for not_permutation in self.not_permutations:
            self.assertFalse(is_permutation_of_palindrome(not_permutation))

if __name__ == "__main__":
    unittest.main()