import unittest


def number_swapper(a, b): 
    a ^= b
    b ^= a
    a ^= b

    return a, b


class Test(unittest.TestCase):
    def test_number_swapper(self):
        print('test')
        self.assertEqual((0, 0), number_swapper(0, 0))
        self.assertEqual((2, 2), number_swapper(2, 2))
        self.assertEqual((9, 3), number_swapper(3, 9))
        self.assertEqual((4, 0), number_swapper(0, 4))


if __name__ == '__main__':
    unittest.main()
