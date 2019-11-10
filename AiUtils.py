from random import sample

                            
def initPopulation(populationSize, cityList):
    population = []

    for i in range(populationSize):
        # Create path
        path = sample(cityList, len(cityList))

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
