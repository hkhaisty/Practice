import unittest


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def check_balanced(root):
    if root is None:
        return 0

    left_height = check_balanced(root.left)
    right_height = check_balanced(root.right)
    if abs(left_height - right_height) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


def is_balanced(root):
    return check_balanced(root) != -1


class Test(unittest.TestCase):
    def test_check_balanced(self):
        root = BinaryTreeNode(10)
        root.left = BinaryTreeNode(5)
        root.right = BinaryTreeNode(20)
        root.left.left = BinaryTreeNode(3)
        root.left.right = BinaryTreeNode(7)
        root.right.left = BinaryTreeNode(15)

        self.assertTrue(is_balanced(root))

        root.left.left.left = BinaryTreeNode(5)

        self.assertTrue(is_balanced(root))

        root.left.left.left.left = BinaryTreeNode(1)

        self.assertFalse(is_balanced(root))


if __name__ == '__main__':
    unittest.main()
