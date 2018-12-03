import unittest


class GraphNode:
    def __init__(self, data):
        self.data = data
        self.adjacent = []
        self.visited = False


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class GraphQueue:
    def __init__(self):
        self.head = None

    def enqueue(self, data):
        if self.head is not None:
            self.head, self.head.next = Node(data), self.head
        else:
            self.head = Node(data)

    def dequeue(self):
        if self.head is None:
            raise Exception('Nothing to dequeue.')

        node = self.head
        self.head = self.head.next
        return node.data

    def is_empty(self):
        return self.head is None


def breadth_first_search(start, end):
    if start == end:
        return True

    queue = GraphQueue()
    queue.enqueue(start)
    while not queue.is_empty():
        node = queue.dequeue()
        if node is not None:
            for adjacent in node.adjacent:
                if not adjacent.visited:
                    if adjacent == end:
                        return True
                    else:
                        queue.enqueue(adjacent)
        node.visited = True
    return False


def route_between(start, end):
    return breadth_first_search(start, end)


class Test(unittest.TestCase):
    def test_route_between(self):
        values = [0, 1, 2, 3, 4, 5]
        nodes = [GraphNode(value) for value in values]
        neighbors = [[1, 4, 5], [3, 4], [1], [2, 4], [], []]
        for i in range(len(neighbors)):
            for neighbor in neighbors[i]:
                nodes[i].adjacent.append(nodes[neighbor])

        routes = [[1, 5], [2, 4], [3, 0], [0, 2], [2, 5]]
        expected = [False, True, False, True, False]
        for route, result in zip(routes, expected):
            for node in nodes:
                node.visited = False
            start, end = route
            self.assertEqual(result, route_between(nodes[start], nodes[end]))


if __name__ == '__main__':
    unittest.main()





