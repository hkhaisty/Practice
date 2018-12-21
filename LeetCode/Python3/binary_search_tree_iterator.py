'''
Solution -- Stack
Runtime Complexity -- amortized O(1)
Space Complexity -- O(h)
'''
class BSTIterator(object):
    def __init__(self, root):
        self.nodes = []
        while root:
            self.nodes.append(root)
            root = root.left

    def hasNext(self):
        return len(self.nodes) > 0

    def next(self):
        node = self.nodes.pop()
        temp = node.right
        while temp:
            self.nodes.append(temp)
            temp = temp.left
            
        return node.val
