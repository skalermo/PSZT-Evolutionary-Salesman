from random import sample

                            
def initPopulation(populationSize, cityList):
    population = []

    for i in range(populationSize):
        # Create path
        path = sample(cityList, len(cityList))

        # Add to list
        population.append(path)

    return population
