import unittest
from Generator import genGraph


class GeneratorTest(unittest.TestCase):
    def test_edgeCount(self):
        g = genGraph(vertexCount=1000, density=0.85)
        edgeCountComplete = 1000 * (1000 - 1) // 2
        edgeCount = int(edgeCountComplete * 0.85)
        self.assertEqual(edgeCount, len(list(g))//2)

    def test_costs(self):
        g = genGraph(vertexCount=1000, density=0.85, costMedian=1000, costDeviation=0.3)

        self.assertTrue(all(edge[2] > 0 for edge in g))


if __name__ == '__main__':
    unittest.main()
