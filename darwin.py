from random import random
from random import seed
from random import randrange

seed(None, 2)
# total number of "genes" per individuals
genome = 20


def control(countdown, pop, generations):
    global fittest
    populationFitness = 0
    # executes for a certain number of generations
    # or until an individual has a fitness of 20
    while countdown < generations and populationFitness != genome:
        newPop = []
        for p in pop:
            if random() > .5:
                selected = selection(pop)
                (child1, child2) = crossover(p, selected)
                child1 = mutate(child1)
                child2 = mutate(child2)
                newPop.append(child1)
                newPop.append(child2)
        newPop = elitism(pop, newPop)
        pop = newPop

        print(f"Epoch {countdown+1}: ")

        individual = 1
        tempfittest = 1
        for p in pop:
            fitness = 0
            for i in p:
                if i == 1:
                    fitness += 1
            print(f"Individual {individual}: {p} Fitness {fitness}")
            individual += 1

            # stores the value for the "fittest" individual in this generation
            if fitness > populationFitness:
                populationFitness = fitness
                fittest = tempfittest
            tempfittest += 1
        countdown += 1

    if populationFitness == 20:
        print(f"We have a winner! #{fittest} is the best after {countdown} generations!")
    else:
        print("Everyone sucked.")


# randomly selects an individual from the population to be used later
def selection(popSelect):
    fitness = 0
    best = 0
    bestFit = []
    for p in popSelect:
        for i in p:
            if i == 1:
                fitness += 1

    for p in popSelect:
        localFitness = 0
        for i in p:
            if i == 1:
                localFitness += 1
        if localFitness > best:
            bestFit = p
        if random() < localFitness/fitness:
            return p

    return bestFit


# creates two new individuals from "crossing" the genome of the "father" and "mother"
def crossover(father, mother):
    # "children" arrays
    first = []
    second = []
    for j in range(genome):
        if j < genome/2:
            first.append(mother[j])
            second.append(father[j])
        else:
            second.append(mother[j])
            first.append(father[j])
    return first, second


# given a 10% chance to mutate a "gene"
def mutate(ind):
    rand = randrange(0, 10)
    if rand == 3:
        i = randrange(0, 20)
        if ind[i] == 0:
            ind[i] = 1
        else:
            ind[i] = 0
    return ind


# not technically an evolutionary thing, but it picks the best individual from
# the last generation and returns to to ensure it is in the next generation
def elitism(population, newPopulation):
    global best
    quality = 0
    for individual in population:
        tally = 0
        for i in individual:
            if i == 1:
                tally += 1
        if tally > quality:
            quality = tally
            best = individual
    newPopulation.append(best)
    return newPopulation


def main():
    pop = [[], [], [], [], [], [], [], [], [], []]

    generations = int(input("How many generations do you wish to run: "))

    for x in range(len(pop)):
        for y in range(genome):
            i = 0
            if random() > .5:
                i = 1
            pop[x].append(i)

    control(0, pop, generations)


main()
