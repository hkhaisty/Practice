import unittest


def binary_to_string(number):
    if number <= 0 or number >= 1:
        return 'ERROR'

    binary = ['.']
    while number > 0:
        if len(binary) >= 32:
            return 'ERROR'

        number *= 2
        if number >= 1:
            binary.append('1')
            number -= 1
        else:
            binary.append('0')

    return ''.join(binary)


class Test(unittest.TestCase):
    def test_binary_to_string(self):
        self.assertEqual('.101', binary_to_string(0.625))
        self.assertEqual('.0101', binary_to_string(0.3125))
        self.assertEqual('ERROR', binary_to_string(0.72))


if __name__ == '__main__':
    unittest.main()
