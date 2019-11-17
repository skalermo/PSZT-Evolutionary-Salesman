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

    def test_negativeCosts(self):
        vc = 1000
        d = 1.0
        g = genGraph(vertexCount=vc, density=d, costMedian=1, costDeviation=1000)

        self.assertFalse(any(edge[2] < 1 for edge in g))

    def test_addCitiesNames(self):
        citiesList = ['Billings',
                      'Boise',
                      'Boston',
                      'Boulder',
                      'Bridgeport',
                      'Brownsville',
                      'Buffalo',
                      'Burbank',
                      'New York',
                      'Columbus']
        g = genGraph(vertexCount=10, density=0.5, citiesNameList=citiesList)
        self.assertTrue(all(city in g.vertices() for city in citiesList))

    def test_genDifferentGraphs(self):
        g = genGraph(vertexCount=100, density=0.6)
        f = genGraph(vertexCount=100, density=0.6)
        self.assertFalse(g.graph == f.graph)

    def test_seed(self):
        g = genGraph(vertexCount=100, density=0.6, seed=1)
        f = genGraph(vertexCount=100, density=0.6, seed=1)
        self.assertTrue(g.graph == f.graph)

        h = genGraph(vertexCount=100, density=0.6, seed=2)
        self.assertFalse(g.graph == h.graph)


if __name__ == '__main__':
    unittest.main()
