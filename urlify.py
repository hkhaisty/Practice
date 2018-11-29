import unittest


def urlify(string, true_length):
    chars = list(string)
    lastIndex = -1
    for i in range(true_length - 1, -1, -1):
        if chars[i] == ' ':
            chars[lastIndex - 2 : lastIndex + 1] = '%20'
            lastIndex -= 3
        else:
            chars[lastIndex] = chars[i]
            lastIndex -= 1
    
    return ''.join(chars)


class Test(unittest.TestCase):
    test = ('caleb mccreary.com  ', 18)
    expected = 'caleb%20mccreary.com'

    def test_urlify(self):
        self.assertEqual(self.expected, urlify(self.test[0], self.test[1]))

if __name__ == "__main__":
    unittest.main()