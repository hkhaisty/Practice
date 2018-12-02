def in_order_traversal(node):
    if node is not None:
        print(node.data)
        in_order_traversal(node.left)
        in_order_traversal(node.right)


def pre_order_traversal(node):
    if node is not None:
        print(node.data)
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)


def post_order_traversal(node):
    if node is not None:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data)

