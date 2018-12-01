import unittest


def compress_string(string):
    compressed = []
    i = 0
    while i < len(string):
        charCount = 0
        j = i
        while j < len(string) and string[j] == string[i]:
            charCount += 1
            j += 1
        compressed.append(string[i])
        compressed.append(str(charCount))
        i = j
    
    return ''.join(compressed) if len(compressed) < len(string) else string


class Test(unittest.TestCase):
    test_string = 'aabcccccaaa'
    expected = 'a2b1c5a3'

    def test_compress_string(self):
        self.assertEqual(self.expected, compress_string(self.test_string))


if __name__ == "__main__":
    unittest.main()