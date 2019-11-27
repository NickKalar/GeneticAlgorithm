from random import random
from random import seed
from random import randrange

seed(None, 2)
# total number of "genes" per individuals
genome = 20
# total number of generations to be ran
generations = 10


def control(countdown, pop):
    while countdown < generations:
        newpop = []
        for p in pop:
            if random() > .5:
                c = selection(pop)
                (a, b) = crossover(p, c)
                a = mutate(a)
                b = mutate(b)
                newpop.append(a)
                newpop.append(b)
        newpop = elitism(pop, newpop)
        pop = newpop

        print(f"Epoch {countdown+1}: ")

        individual = 1
        for p in pop:
            fitness = 0
            for i in p:
                if i == 1:
                    fitness += 1
            print(f"Individual {individual}: {p} Fitness {fitness}")
            individual += 1
        countdown += 1


# randomly selects an individual from the population to be used later
def selection(popSelect):
    rand = randrange(0, len(popSelect))
    return popSelect[int(rand)]


# creates two new individuals from "crossing" the genome of the "father" and "mother"
def crossover(father, mother):
    first = []
    last = []
    for j in range(genome):
        if genome < 10:
            first.append(mother[j])
            last.append(father[j])
        else:
            last.append(mother[j])
            first.append(father[j])
    return first, last


# given a 10% chance to mutate any "gene"
def mutate(ind):
    for i in ind:
        rand = randrange(0, 9)
        if rand == 1:
            if i == 0:
                i = 1
            else:
                i = 0
    return ind


# not technically an evolutionary thing, but it picks the best individual from
# the last generation and returns to to ensure it is in the next generation
def elitism(p, np):
    global best
    for n in p:
        q = 0
        t = 0
        for i in n:
            if i == 1:
                t += 1
        if t > q:
            best = n
    np.append(best)
    return np


def main():
    countdown = 0
    pop = [[], [], [], [], [], [], [], [], [], []]

    for x in range(10):
        for y in range(20):
            i = 0
            if random() > .5:
                i = 1
            pop[x].append(i)

    control(countdown, pop)


main()
