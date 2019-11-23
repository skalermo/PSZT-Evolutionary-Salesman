import unittest


from Main import evolutionaryAlgorithm
from Generator import genGraph
from Graph import WeightedGraph


class MyTestCase(unittest.TestCase):
    def test_evolutionaryAlgorithm(self):
        n = 20
        singleTravelCost = 1
        graph = genGraph(vertexCount=n, density=1.0)

        addCheapestCycle(graph, singleTravelCost)
        _, distance = evolutionaryAlgorithm(graph, 1000, 4, 0.1)
        self.assertTrue(n * singleTravelCost, distance)

    def test_addCheapestCycle(self):
        n = 10
        graph = WeightedGraph()
        for i in range(n):
            graph.addVertex(i)

        addCheapestCycle(graph, 1)
        self.assertTrue(all(e[2] == 1 for e in graph))


def addCheapestCycle(graph, cheapCost):
    n = len(graph.vertices())
    overwriteEdge(graph, n - 1, 0, cheapCost)
    for i in range(n-1):
        overwriteEdge(graph, i, i + 1, cheapCost)


def overwriteEdge(graph, v1, v2, cost):
    if v1 not in graph.graph:
        graph.graph[v1] = {v2: cost}

    if v2 not in graph.graph:
        graph.graph[v2] = {v1: cost}

    graph.graph[v1][v2] = cost
    graph.graph[v2][v1] = cost


if __name__ == '__main__':
    unittest.main()
