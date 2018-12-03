import unittest


def insertion(m, n, i, j):
    mask = (-1 << (j + 1)) | (1 << (i - 1))
    return (n & mask) | (m << i)


class Test(unittest.TestCase):
    def test_insertion(self):
        self.assertEqual(1100, insertion(19, 2**10, 2, 6))


if __name__ == '__main__':
    unittest.main()
