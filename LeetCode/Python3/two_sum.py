import unittest

'''
Solution -- Hash Table Implementation
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


class Test(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual([0, 1], two_sum([2, 7, 11, 15], 9))
        self.assertIsNone(two_sum([2, 7, 11, 15], 8))
        self.assertEqual([2, 8], two_sum([0, 88, -1, 3, 21, 6, 10, 19, 5, 52], 4))

if __name__ == '__main__':
    unittest.main()