import unittest
import random

from Generator import genGraph
from Graph import WeightedGraph
import AiUtils


class AiUtilsTest(unittest.TestCase):
    def setUp(self):
        self.g = WeightedGraph()

    def test_calcDistance(self):
        self.g.addEdge('a', 'b', 12)
        self.g.addEdge('a', 'c', 3)
        self.g.addEdge('b', 'd', 5)
        self.g.addEdge('b', 'c', 6)
        self.g.addEdge('b', 'd', 4)

        path = random.sample(self.g.vertices(), len(self.g.vertices()))
        pathDist = AiUtils.calcDistance(self.g, path)
        self.assertEqual(-1, pathDist)

        self.g.addEdge('c', 'd', 7)
        self.g.addEdge('d', 'a', 8)
        pathDist = AiUtils.calcDistance(self.g, path)
        self.assertTrue(pathDist > 0)

    def test_calcFitness(self):
        self.g.addEdge('a', 'b', 10)
        self.g.addEdge('c', 'a', 3)

        path = AiUtils.genPath(self.g.vertices())
        fitness = AiUtils.calcFitness(self.g, path)
        self.assertEqual(-1, fitness)

        self.g.addEdge('b', 'c', 5)
        path = AiUtils.genPath(self.g.vertices())
        fitness = AiUtils.calcFitness(self.g, path)
        self.assertTrue(fitness == 1.0/18)

    def test_rankPaths(self):
        self.fail()

    def test_selection(self):
        self.g = genGraph(100, 1)

        population = AiUtils.initPopulation(100, self.g.vertices())
        ranked = AiUtils.rankPaths(self.g, population)

        with self.assertRaises(Exception) as context:
            AiUtils.selection(ranked, 30, selectionSize=1.1)

            self.assertTrue('Selection size must be in [0 .. 1]' in context.exception)




if __name__ == '__main__':
    unittest.main()
