import unittest


def permutations_without_duplicates(str):
    if str is None:
        return None

    permutations = []
    if len(str) == 0:
        permutations.append('')
        return permutations

    first, remainder = str[0], str[1:]
    perms = permutations_without_duplicates(remainder)
    for perm in perms:
        for j in range(len(perm) + 1):
            s = perm[:j] + first + perm[j:]
            permutations.append(s)

    return permutations


class Test(unittest.TestCase):
    def test_permutations(self):
       self.assertIsNone(permutations_without_duplicates(None))
       self.assertEqual([''], permutations_without_duplicates(''))
       self.assertEqual(['a'], permutations_without_duplicates('a'))
       self.assertEqual(['ab', 'ba'], permutations_without_duplicates('ab'))
       expected = ['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
       self.assertEqual(expected, permutations_without_duplicates('abc'))

if __name__ == '__main__':
    unittest.main()
