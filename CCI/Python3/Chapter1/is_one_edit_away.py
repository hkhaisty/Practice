import unittest


def is_one_edit_away(string1, string2):
    if abs(len(string1) - len(string2)) > 1:
        return False

    shorter = string1 if len(string1) < len(string2) else string2
    longer = string1 if shorter == string2 else string2
    sIndex = lIndex = charDiff = 0
    while sIndex < len(shorter) and lIndex < len(longer):
        if shorter[sIndex] != longer[lIndex]:
            charDiff += 1
            if charDiff > 1:
                return False
            if len(shorter) == len(longer):
                sIndex += 1
        else:
            sIndex += 1

        lIndex += 1
    
    return True


class Test(unittest.TestCase):
    test_string = 'pale'
    one_edit_away = ['ple', 'pales', 'bale', 'kale', 'ale']
    not_one_edit_away = ['pallet', 'bake', 'rail', 'tall', 'baler']

    def test_one_edit_away(self):
        for edit in self.one_edit_away:
            self.assertTrue(is_one_edit_away(self.test_string, edit))
        
    def test_not_one_edit_away(self):
        for edit in self.not_one_edit_away:
            self.assertFalse(is_one_edit_away(self.test_string, edit))

if __name__ == "__main__":
    unittest.main()