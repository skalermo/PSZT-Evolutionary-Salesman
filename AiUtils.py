import random
import numpy as np


def genPath(cityList):
    return random.sample(cityList, len(cityList))


def initPopulation(populationSize, cityList):
    population = []

    for i in range(populationSize):
        # Create path
        path = genPath(cityList)

        # Add to list
        population.append(path)

    return population


def calcDistance(graph, path):
    """Sum distances between cities in a route
    If route is invalid return -1 as distance"""

    pathDistance = 0
    for i in range(0, len(path)):
        fromCity = path[i]
        toCity = path[i + 1] if i + 1 < len(path) else path[0]

        distance = graph[fromCity, toCity]
        if distance:
            pathDistance += distance
        else:
            return -1
    return pathDistance


def calcFitness(graph, path):
    return 1 / float(calcDistance(graph, path))


def rankPaths(graph, population):
    fitnessResults = {}
    for i in range(0, len(population)):
        fitnessResults[i] = calcFitness(graph, population[i])
    return sorted(fitnessResults.items(), key=lambda elem: elem[1], reverse=True)


def selection(ranked, eliteSize, selectionSize=0.5):
    """Select parents for next generation using Elitism and Roulette Wheel Selection"""
    if not 0 < selectionSize <= 1:
        raise Exception('Selection size must be in [0 .. 1]')

    # Filter out -1 fitness
    # ranked = [x for x in ranked if x[1] > 0]

    selected = []

    # Choose elite
    for i in range(eliteSize):
        selected.append(ranked[i][0])

    # Prepare probabilities for roulette wheel selection
    fitnessList = [fit for _, fit in ranked[eliteSize:]]
    fitnessCumSum = np.cumsum(fitnessList)
    fitnessSum = np.sum(fitnessList)
    fitnessProbability = [fit / fitnessSum for fit in fitnessCumSum]

    # Roulette wheel selection
    for x in range(int(len(ranked)*selectionSize) - eliteSize):
        pick = random.random()

        for i in range(eliteSize, len(ranked)):
            if pick <= fitnessProbability[i]:
                selected.append(ranked[i][0])
                break

    return selected


def matingPool(population, selectionResults):
    """Extract population from selectionResults"""
    pool = []

    for index in selectionResults:
        pool.append(population[index])

    return pool


def breed(parent1, parent2):
    """Give birth to 2 children based on material from the parents"""

    # randomly select the consecutive genes (chain)
    # by picking the first and last genes
    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    # create chains of selected genes for 2 children
    chain1 = []
    chain2 = []
    for i in range(startGene, endGene+1):
        chain1.append(parent1[i])
        chain2.append(parent2[i])

    # fill the remaining empty slots with genes from another parent
    child1 = chain1 + [gene for gene in parent2 if gene not in chain1]
    child2 = chain2 + [gene for gene in parent1 if gene not in chain2]

    return child1, child2


def breedPopulation(matingPool, eliteSize):
    """Produce children from elite and by breeding
    matingPool is changed by this function !"""

    children = []

    # add elite to children
    for i in range(0, eliteSize):
        children.append(matingPool[i])

    # shuffle mating pool
    random.shuffle(matingPool)

    # breed new and add them to children
    for i in range(0, len(matingPool)):
        bornChildren = breed(matingPool[i], matingPool[-i-1])
        children.extend(bornChildren)

    return children

