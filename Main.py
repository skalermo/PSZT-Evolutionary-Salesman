import argparse
from time import time
from sys import stdout
from Generator import genGraph
from AiUtils import nextGeneration, initPopulation, calcDistance
from Graph import WeightedGraph as Graph


def evolutionaryAlgorithm(graph, generations, eliteSize, mutationRate):
    popSizeRate = 0.6
    popSize = int(len(graph.vertices()) * popSizeRate)
    population = initPopulation(popSize, graph.vertices())
    lastDistance = -1
    lastGeneration = 0
    try:
        for i in range(generations):
            population = nextGeneration(graph, population, eliteSize, mutationRate)
            distance = calcDistance(graph, population[0])

            if lastDistance != distance:
                print()

            stdout.write(u"\u001b[1000DGeneration:{} Distance:{} ".format(i, distance))
            stdout.flush()

            lastDistance = distance
            lastGeneration = i
    finally:
        return population[0], calcDistance(graph, population[0]), lastGeneration


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog='Main.py', description='Evolutionary algorithm')
    parser.add_argument('-n', type=int, metavar='', help='Number of vertices')
    parser.add_argument('-d', type=float, default=1.0, metavar='', help='Density of the graph')
    parser.add_argument('-s', type=float, default=None, metavar='', help='Seed for generator')
    parser.add_argument('-g', type=int, default=50, metavar='', help='Number of generations')
    parser.add_argument('-e', type=int, default=None, metavar='', help='Number of elite individuals')
    parser.add_argument('-m', type=float, default=None, metavar='', help='Chance of mutation on given gene')
    parser.add_argument('-i', type=str, metavar='', help='Input file')
    parser.add_argument('-o', type=str, default=None, metavar='', help='Output file')

    args = vars(parser.parse_args())
    graph = None
    if args['n'] is None and args['i'] is None:
        parser.print_help()
        exit(1)

    vertexCount = 0
    if args['n']:
        vertexCount = args['n']
        density = args['d']
        seed = args['s']
        graph = genGraph(vertexCount, density, costMedian=10, costDeviation=5, seed=seed)

    if args['i']:
        graph = Graph.load(args['i'])
        vertexCount = len(graph.vertices())

    generations = args['g']
    eliteSize = args['e']
    if eliteSize is None:
        eliteSize = int(vertexCount * 0.3)

    mutationRate = args['m']
    if mutationRate is None:
        mutationRate = 10.0 / vertexCount

    startTime = time()

    bestPath, bestDistance, lastGeneration = evolutionaryAlgorithm(graph, generations, eliteSize, mutationRate)

    end = int((time() - startTime) * 1000)
    print('\nTime: {}m {}s {}ms'.format((end // 60000), (end // 1000) % 60, end % 1000))
    if args['o'] is None:
        print(str(bestPath) + ' ' + str(bestDistance))
    else:
        with open(args['o'], 'w') as output:
            output.write('Last generation: {}, Distance: {}\n'.format(lastGeneration, bestDistance))
            output.write('Path: {}, \' {}\' \n'.format(str(bestPath)[1:-1], str(bestPath[0])))
