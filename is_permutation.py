import unittest


def is_permutation(string1, string2):
    if len(string1) is not len(string2):
        return False

    found_characters = 0
    for char1, char2 in zip(string1, string2):
        char1 = ord(char1)
        char2 = ord(char2)
        found_characters ^= char1 ^ char2
    
    return found_characters == 0


class Test(unittest.TestCase):
    test_string = 'outdoors'
    permutations = ['doorouts', 'stoudoor', 'roodstou', 'srootdou', 'rotsodou']
    not_permutations = ['donut', 'inside', 'outside', 'plant', '']

    def test_permutations(self):
        for permutation in self.permutations:
            self.assertTrue(is_permutation(self.test_string, permutation))

        for not_permutation in self.not_permutations:
            self.assertFalse(is_permutation(self.test_string, not_permutation))

if __name__ == "__main__":
    unittest.main()
