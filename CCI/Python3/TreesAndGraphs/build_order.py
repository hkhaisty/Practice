import unittest


class Project:
    def __init__(self, data):
        self.data = data
        self._dependencies = {}
        self.num_dependencies = 0

    def add_dependency(self, dependency):
        if dependency not in self._dependencies:
            self._dependencies[dependency] = dependency
            self.num_dependencies += 1


class Graph:
    def __init__(self):
        self.projects = []


def build_graph(values, edges):
    graph = Graph()
    for data, dependencies in zip(values, edges):
        project = Project(data)
        for dependency in dependencies:
            project.add_dependency(dependency)
        graph.projects.append(project)

    return graph


def build_order(graph):
    build = []
    for project in graph.projects:
        if project.num_dependencies == 0:
            build.append(project)

    return build


class Test(unittest.TestCase):
    def test_build_order(self):
        projects = ['a', 'b', 'c', 'd', 'e', 'f']
        dependencies = [['f'], ['f'], ['d'], ['a', 'b'], [], []]
        graph = build_graph(projects, dependencies)
        expected = ['e', 'f', 'a', 'b', 'd', 'c']



if __name__ == '__main__':
    unittest.main()