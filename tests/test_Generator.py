import unittest
from Generator import genGraph


class GeneratorTest(unittest.TestCase):
    def test_edgeCount(self):
        g = genGraph(vertexCount=1000)
        edgeCount = 1000 * (1000 - 1) // 2
        self.assertEqual(edgeCount, len(list(g))//2)

    def test_costs(self):
        vc = 1000
        g = genGraph(vertexCount=vc, costMedian=1000, costDeviation=100)
        self.assertTrue(all(edge[2] > 0 for edge in g))
        edgesInRange = sum(900 < edge[2] < 1100 for edge in g)
        edgeCount = vc * (vc - 1) // 2
        self.assertTrue(edgesInRange > edgeCount * 0.97)

    def test_negativeCosts(self):
        vc = 1000
        g = genGraph(vertexCount=vc, costMedian=1, costDeviation=1000)

        self.assertFalse(any(edge[2] < 1 for edge in g))

    def test_genDifferentGraphs(self):
        g = genGraph(vertexCount=100, seed=1)
        f = genGraph(vertexCount=100, seed=2)
        self.assertFalse(g.graph == f.graph)

    def test_seed(self):
        g = genGraph(vertexCount=100, seed=1)
        f = genGraph(vertexCount=100, seed=1)
        self.assertTrue(g.graph == f.graph)


if __name__ == '__main__':
    unittest.main()
