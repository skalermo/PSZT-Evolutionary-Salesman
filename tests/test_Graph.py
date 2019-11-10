import unittest
from Graph import WeightedGraph


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.g = WeightedGraph()

    def test_addVertex(self):
        self.g.addVertex('a')
        self.g.addVertex('a')
        self.g.addVertex('b')

        self.assertEqual(2, len(self.g.vertices()))

    def test_addEdge(self):
        self.g.addEdge('a', 'b', 2)
        self.g.addEdge('a', 'c', 3)
        self.g.addEdge('a', 'b', 5)

        self.assertEqual(3, len(self.g.vertices()))

    def test_iter(self):
        self.g.addEdge('a', 'd', 2)
        self.g.addEdge('b', 'c', 3)
        self.g.addEdge('a', 'b', 5)
        self.g.addEdge('a', 'b', 3)

        self.assertTrue(('a', 'd', 2) in self.g)
        self.assertTrue(('b', 'c', 3) in self.g)
        self.assertFalse(('a', 'b', 3) in self.g)
        self.assertEqual(3, len(list(self.g))//2)

    def test_getItem(self):
        self.g.addEdge('a', 'b', 1000)
        self.g.addEdge('x', 'y', 2)
        self.assertEqual(1000, self.g[('a', 'b')])
        self.assertEqual(2, self.g['x', 'y'])
        self.assertEqual(None, self.g['a', 'x'])


if __name__ == '__main__':
    unittest.main()
