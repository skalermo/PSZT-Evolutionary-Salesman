from time import time
import random
import numpy as np
import argparse
from sys import stdout


import Graph


def genGraph(vertexCount, density, costMedian=100, costDeviation=10, citiesNameList=None, seed=None):
    """Generate weighted graph based on parameters
    :param vertexCount Number of vertices to generate
    :param density Ratio of number of edges in the graph
to the number of edges in a N complete graph
    :param costMedian 'Centre' of cost distribution
    :param costDeviation 'Spread' of distribution
    :param citiesNameList List of names of cities (optional)
    :param seed For numpy random
    :return Generated graph"""

    if seed is None:
        seed = time()
    random.seed(seed)
    np.random.seed(int(seed))

    g = Graph.WeightedGraph()

    # Calculate number of edges to generate based on density
    edgeCountComplete = int(vertexCount * (vertexCount - 1) / 2)
    edgeCountToGenerate = int(edgeCountComplete * density)

    # Pick random edges
    edgesWithoutCosts = random.sample([(str(i), str(j),) for i in range(vertexCount - 1)
                                       for j in range(i + 1, vertexCount)], edgeCountToGenerate)

    # Use cities' names instead of numbers
    if citiesNameList and len(citiesNameList) >= vertexCount:
        edgesWithoutCosts = [(citiesNameList[i], citiesNameList[j]) for i, j in edgesWithoutCosts]

    # Calculate costs from integer normal distribution
    costs = list(np.random.normal(costMedian, costDeviation, edgeCountToGenerate).astype(int))

    for edge, cost in zip(edgesWithoutCosts, costs):
        g.addEdge(str(edge[0]), str(edge[1]), cost.item() if cost > 1 else 1)

    return g


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Generator.py', description='Graph generator')
    parser.add_argument('-n', type=int, metavar='', help='Number of vertices')
    parser.add_argument('-d', type=float, default=1.0, metavar='', help='Density of the graph')
    parser.add_argument('-s', type=float, default=None, metavar='', help='Seed for generator')
    parser.add_argument('-M', type=int, default=100, metavar='', help='Cost median')
    parser.add_argument('-D', type=int, default=10, metavar='', help='Cost deviation')

    args = vars(parser.parse_args())
    if args['n'] is None:
        parser.print_help()
        exit(1)

    vertexCount = args['n']
    density = args['d']
    seed = args['s']
    costMedian = args['M']
    costDeviation = args['D']

    g = genGraph(vertexCount, density, costMedian, costDeviation, seed=seed)
    g.dump(stdout)

