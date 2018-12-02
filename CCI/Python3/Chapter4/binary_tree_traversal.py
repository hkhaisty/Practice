from binary_tree_node import BinaryTreeNode


def in_order_traversal(node, values):
    if node is not None:
        in_order_traversal(node.left, values)
        values.append(node.data)
        in_order_traversal(node.right, values)


def pre_order_traversal(node, values):
    if node is not None:
        values.append(node.data)
        pre_order_traversal(node.left, values)
        pre_order_traversal(node.right, values)


def post_order_traversal(node, values):
    if node is not None:
        post_order_traversal(node.left, values)
        post_order_traversal(node.right, values)
        values.append(node.data)


if __name__ == '__main__':
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(5)
    root.left.left = BinaryTreeNode(9)
    root.left.right = BinaryTreeNode(18)
    root.right = BinaryTreeNode(20)
    root.right.left = BinaryTreeNode(3)
    root.right.right = BinaryTreeNode(7)

    print('Original tree, flattened:')
    print([10, 5, 9, 18, 20, 3, 7])
    print('In Order Traversal:')
    values = []
    in_order_traversal(root, values)
    print(values)
    print('Pre Order Traversal:')
    values = []
    pre_order_traversal(root, values)
    print(values)
    print('Post Order Traversal:')
    values = []
    post_order_traversal(root, values)
    print(values)

