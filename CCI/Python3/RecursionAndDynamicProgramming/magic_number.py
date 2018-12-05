import unittest


def search_distinct(nums, start, end):
    if end < start:
        return -1

    middle = (start + end) // 2
    if nums[middle] == middle:
        return middle 
    elif nums[middle] < middle:
        return search(nums, middle + 1, end)
    else:
        return search(nums, start, middle - 1)


def magic_number_distinct(nums):
    if not nums or len(nums) == 0:
        return None

    return search(nums, 0, len(nums) - 1)



def search(nums, start, end):
    if end < start:
        return -1

    middle = (start + end) // 2
    if nums[middle] == middle:
        return middle 

    left = search(nums, start, min(middle - 1, nums[middle]))
    if left >= 0:
        return left
    
    right = search(nums, max(middle + 1, nums[middle]), end)

    return right 


def magic_number(nums):
    if not nums or len(nums) == 0:
        return None

    return search(nums, 0, len(nums) - 1)    
    

class Test(unittest.TestCase):
    def test_magic_number_distinct(self):
        self.assertIsNone(magic_number_distinct(None))
        self.assertIsNone(magic_number_distinct([]))
        self.assertEqual(-1, magic_number_distinct([1]))
        self.assertEqual(6, magic_number_distinct([-5, -2, -1, 2, 3, 4, 6, 10, 12, 14]))

    def test_magic_number(self):
        self.assertIsNone(magic_number_distinct(None))
        self.assertIsNone(magic_number_distinct([]))
        self.assertEqual(-1, magic_number_distinct([1]))
        self.assertEqual(2, magic_number_distinct([-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]))
        self.assertEqual(7, magic_number_distinct([-10, -5, 1, 2, 2, 3, 4, 7, 9, 12, 13]))


if __name__ == '__main__':
    unittest.main()
        