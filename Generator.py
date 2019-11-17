from time import time
import random
import numpy as np


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
    edgesWithoutCosts = random.sample([(i, j,) for i in range(vertexCount - 1)
                                       for j in range(i + 1, vertexCount)], edgeCountToGenerate)

    # Use cities' names instead of numbers
    if citiesNameList and len(citiesNameList) >= vertexCount:
        edgesWithoutCosts = [(citiesNameList[i], citiesNameList[j]) for i, j in edgesWithoutCosts]

    # Calculate costs from integer normal distribution
    costs = list(np.random.normal(costMedian, costDeviation, edgeCountToGenerate).round().astype(np.int))

    for edge, cost in zip(edgesWithoutCosts, costs):
        g.addEdge(edge[0], edge[1], cost if cost > 1 else 1)

    return g

