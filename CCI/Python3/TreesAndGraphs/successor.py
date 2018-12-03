import unittest
import minimal_tree


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


def successor(root, target, found=None):
    if found is not None:
        return found

    if root is None:
        return None

    found = successor(root.left, target, found)

    if root.parent == target:
        return root

    found = successor(root.right, target, found)

    return found


class Test(unittest.TestCase):
    def test_successor(self):
        root = BinaryTreeNode(4)
        root.left = BinaryTreeNode(3)
        root.left.parent = root
        root.right = BinaryTreeNode(5)
        root.right.parent = root
        root.right.left = BinaryTreeNode(6)
        root.right.left.parent = root.right
        root.right.right = BinaryTreeNode(10)
        root.right.right.parent = root.right

        self.assertEqual(root.right.left, successor(root, root.right))


if __name__ == '__main__':
    unittest.main()
