import unittest

def sorted_merge(a, b, size_a):
    index_a = size_a - 1
    index_b = len(b) - 1
    index = len(a) - 1
    while index_b >= 0:
        if index_a >= 0 and a[index_a] > b[index_b]:
            a[index] = a[index_a]
            index_a -= 1
        else:
            a[index] = b[index_b]
            index_b -= 1
        index -= 1


class Test(unittest.TestCase):
    def test_sorted_merge(self):
        a = [2, 4, 5, 9, 0, 0, 0]
        b = [3, 7, 11] 
        expected = [2, 3, 4, 5, 7, 9, 11]
        sorted_merge(a, b, 4)

        self.assertEqual(expected, a)

if __name__ == '__main__':
    unittest.main()