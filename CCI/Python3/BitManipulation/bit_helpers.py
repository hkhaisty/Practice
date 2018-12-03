import unittest


def get_bit(number, index):
    return 1 if (number & (1 << index)) != 0 else 0


def set_bit(number, index):
    return number | (1 << index)


def clear_bit(number, index):
    return number & ~(1 << index)


def clear_bits_msb_to_index(number, index):
    return number & ((1 << index) - 1)


def clear_bits_index_to_0(number, index):
    return number & (-1 << (index + 1))


def update_bit(number, index, value):
    return (number & ~(1 << index)) | (value << index)


class Test(unittest.TestCase):
    def test_get_bit(self):
        self.assertEqual(0, get_bit(4, 0))
        self.assertEqual(0, get_bit(4, 1))
        self.assertEqual(1, get_bit(4, 2))

    def test_set_bit(self):
        self.assertEqual(5, set_bit(4, 0))
        self.assertEqual(6, set_bit(4, 1))
        self.assertEqual(7, set_bit(6, 0))

    def test_clear_bit(self):
        self.assertEqual(0, clear_bit(4, 2))
        self.assertEqual(5, clear_bit(7, 1))
        self.assertEqual(6, clear_bit(7, 0))

    def test_clear_bit_to_index(self):
        self.assertEqual(0, clear_bits_msb_to_index(7, 0))
        self.assertEqual(1, clear_bits_msb_to_index(7, 1))
        self.assertEqual(3, clear_bits_msb_to_index(7, 2))

    def test_clear_bits_index_to_0(self):
        self.assertEqual(0, clear_bits_index_to_0(7, 2))
        self.assertEqual(4, clear_bits_index_to_0(7, 1))
        self.assertEqual(6, clear_bits_index_to_0(7, 0))

    def test_update_bit(self):
        self.assertEqual(6, update_bit(7, 0, 0))
        self.assertEqual(3, update_bit(7, 2, 0))
        self.assertEqual(5, update_bit(4, 0, 1))


if __name__ == '__main__':
    unittest.main()


