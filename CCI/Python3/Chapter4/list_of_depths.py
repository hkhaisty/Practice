import unittest


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_depth_linked_list(node, depths, depth=0):
    if node is None:
        return

    if len(depths) == depth:
        depths.append(Node(node))
    else:
        root = depths[depth]
        while root.next is not None:
            root = root.next
        root.next = Node(node)

    build_depth_linked_list(node.left, depths, depth + 1)
    build_depth_linked_list(node.right, depths, depth + 1)


def list_of_depths(root):
    depths = []
    build_depth_linked_list(root, depths)

    return depths


class Test(unittest.TestCase):
    def test_list_of_depths(self):
        root = BinaryTreeNode(10)
        root.left = BinaryTreeNode(5)
        root.right = BinaryTreeNode(20)
        root.left.left = BinaryTreeNode(3)
        root.left.right = BinaryTreeNode(7)
        root.right.left = BinaryTreeNode(15)

        zero = Node(root)
        one = Node(root.left)
        one.next = Node(root.right)
        two = Node(root.left.left)
        two.next = Node(root.left.right)
        two.next.next = Node(root.right.left)

        expected = [zero, one, two]
        lists = list_of_depths(root)
        for node1, node2 in zip(expected, lists):
            while node1 is not None and node2 is not None:
                self.assertEqual(node1.data, node2.data)
                node1 = node1.next
                node2 = node2.next


if __name__ == '__main__':
    unittest.main()
