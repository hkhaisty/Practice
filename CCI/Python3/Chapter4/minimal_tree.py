import unittest


class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def recurse(arr, start, end):
    if end < start:
        return None

    median = (start + end) // 2
    node = BinaryTreeNode(arr[median])
    node.left = recurse(arr, start, median - 1)
    node.right = recurse(arr, median + 1, end)

    return node


def create_minimal_binary_search_tree(arr):
    return recurse(arr, 0, len(arr) - 1)


def pre_order_flatten(tree, nodes):
    if tree is not None:
        nodes.append(tree.data)
        pre_order_flatten(tree.left, nodes)
        pre_order_flatten(tree.right, nodes)

    return nodes


class Test(unittest.TestCase):
    def test_create_minimal_binary_search_tree(self):
        values = [1, 2, 3, 4, 5, 6, 7]
        expected = [4, 2, 1, 3, 6, 5, 7]
        tree = create_minimal_binary_search_tree(values)
        node_data = pre_order_flatten(tree, [])

        for data, value in zip(node_data, expected):
            self.assertEqual(value, data)


if __name__ == '__main__':
    unittest.main()