import argparse
from time import time
from sys import stdout
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from random import seed as setSeed
import numpy as np


from Generator import genGraph
from AiUtils import nextGeneration, initPopulation, calcDistance
from Graph import WeightedGraph as Graph


def evolutionaryAlgorithm(graph, generations, eliteSize, mutationRate):
    popSizeRate = 0.6
    popSize = int(len(graph.vertices()) * popSizeRate)
    population = initPopulation(popSize, graph.vertices())
    lastDistance = -1
    lastGeneration = 0
    progress = []
    if lastDistance != -1:
        progress.append(calcDistance(graph, population[0]))
    try:
        for i in range(generations):
            population = nextGeneration(graph, population, eliteSize, mutationRate)
            distance = calcDistance(graph, population[0])
            if lastDistance != -1:
                progress.append(calcDistance(graph, population[0]))

            if lastDistance != distance:
                lastDistance = distance
                print()

            stdout.write(u"\u001b[1000DGeneration:{} Distance:{} ".format(i, distance))
            stdout.flush()

            lastGeneration = i
    finally:
        return population[0], progress, lastGeneration


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
    parser.add_argument('-c', action='store_true', default=False, help='Output a chart')

    args = vars(parser.parse_args())
    graph = None
    if args['n'] is None and args['i'] is None:
        parser.print_help()
        exit(1)

    seed = args['s']

    vertexCount = 0
    if args['n']:
        vertexCount = args['n']
        density = args['d']
        graph = genGraph(vertexCount, density, costMedian=10, costDeviation=5, seed=seed)

    if args['i']:
        graph = Graph.load(args['i'])
        vertexCount = len(graph.vertices())
        setSeed(seed)

    generations = args['g']
    eliteSize = args['e']
    if eliteSize is None:
        eliteSize = int(vertexCount * 0.3)

    mutationRate = args['m']
    if mutationRate is None:
        mutationRate = 10.0 / vertexCount

    startTime = time()
    bestPath, progress, lastGeneration = evolutionaryAlgorithm(graph, generations, eliteSize, mutationRate)
    end = int((time() - startTime) * 1000)

    # check if there is any progress at all
    bestDistance = -1 if len(progress) == 0 else progress[-1]
    print('\nTime: {}m {}s {}ms'.format((end // 60000), (end // 1000) % 60, end % 1000))
    if args['o'] is None:
        if bestDistance == -1:
            print('No path found')
            exit()
        else:
            print('Last generation: {}, Distance: {}\n'.format(lastGeneration, bestDistance))
            print('Path: {}, \' {}\' \n'.format(str(bestPath)[1:-1], str(bestPath[0])))
    else:
        with open(args['o'], 'w') as output:
            if bestDistance == -1:
                output.write('No path found')
                exit()
            else:
                output.write('Last generation: {}, Distance: {}\n'.format(lastGeneration, bestDistance))
                output.write('Path: {}, \' {}\' \n'.format(str(bestPath)[1:-1], str(bestPath[0])))

    if args['c']:
        # the generation where some progress has appeared
        firstGoodGeneration = lastGeneration - len(progress)

        fig, ax = plt.subplots()
        ax.plot(list(range(firstGoodGeneration, len(progress) + firstGoodGeneration)), progress)

        # draw a tick corresponding to the firstGoodGeneration above the chart
        generationTick = [firstGoodGeneration]
        ax.xaxis.set_minor_locator(ticker.FixedLocator(generationTick))
        ax.xaxis.set_minor_formatter(ticker.FixedFormatter(generationTick))
        ax.tick_params(axis="x", which="minor", direction="out",
                       top=True, labeltop=True, bottom=False, labelbottom=False)

        # draw a tick corresponding to the the lowest achieved cost
        costTick = [progress[-1]]
        ax.yaxis.set_minor_locator(ticker.FixedLocator(costTick))
        ax.yaxis.set_minor_formatter(ticker.FixedFormatter(costTick))
        ax.tick_params(axis="y", which="minor", direction="out",
                       right=True, labelright=True, left=False, labelleft=False)

        ax.set_ylabel('Distance')
        ax.set_xlabel('Generation')

        # save chart
        fig.set_size_inches(18, 10, forward=True)
        fig.set_dpi(100)
        fig.savefig('chart.png', dpi=100)

        plt.show()
        plt.close()
