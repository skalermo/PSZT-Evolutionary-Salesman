import unittest
from Generator import genGraph


class GeneratorTest(unittest.TestCase):
    def test_edgeCount(self):
        g = genGraph(vertexCount=1000, density=0.85)
        edgeCountComplete = 1000 * (1000 - 1) // 2
        edgeCount = int(edgeCountComplete * 0.85)
        self.assertEqual(edgeCount, len(list(g))//2)

    def test_costs(self):
        vc = 1000
        d = 0.85
        g = genGraph(vertexCount=vc, density=d, costMedian=1000, costDeviation=100)
        self.assertTrue(all(edge[2] > 0 for edge in g))
        edgesInRange = sum(900 < edge[2] < 1100 for edge in g)
        edgeCountComplete = vc * (vc - 1) // 2
        edgeCount = int(edgeCountComplete * d)
        self.assertTrue(edgesInRange > edgeCount * 0.97)


if __name__ == '__main__':
    unittest.main()
