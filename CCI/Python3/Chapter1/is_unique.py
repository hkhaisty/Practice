import unittest


def is_unique(string):
    charset_size = 128
    if len(string) > charset_size or not string:
        return False

    found_chars = [False for _ in range(charset_size)]
    for char in string:
        char = ord(char)
        if found_chars[char]:
            return False  

        found_chars[char] = True

    return True


class Test(unittest.TestCase):
    not_unique = ['a2b2d', '5(d*85']
    unique = ['eTnB591&^c', '()-_87dFeT']

    def test_empty_string(self):
        self.assertFalse(is_unique(''))

    def test_not_unique(self):
        for test_string in self.not_unique:
            self.assertFalse(is_unique(test_string))
        
    def test_unique(self):
        for test_string in self.unique:
            self.assertTrue(is_unique(test_string))

if __name__ == '__main__':
    unittest.main()