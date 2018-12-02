import unittest
import minimal_tree


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def validate_bst(root, minimum=None, maximum=None):
    if root is None:
        return True

    if (minimum is not None and root.data <= minimum) or (maximum is not None and root.data > maximum):
        return False

    if not validate_bst(root.left, minimum, root.data) or not validate_bst(root.right, root.data, maximum):
        return False

    return True


class Test(unittest.TestCase):
    def test_validate_bst(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        valid_root = minimal_tree.create_minimal_binary_search_tree(values)
        invalid_root = BinaryTreeNode(3)
        invalid_root.left = BinaryTreeNode(2)
        invalid_root.left.left = BinaryTreeNode(1)
        invalid_root.right = BinaryTreeNode(5)
        invalid_root.right.left = BinaryTreeNode(1)

        self.assertTrue(validate_bst(valid_root))
        self.assertFalse(validate_bst(invalid_root))


if __name__ == '__main__':
    unittest.main()
