from random import random
from random import seed

seed(None, 2)

term = False
pop = [[], [], [], [], [], [], [], [], [], []]

for x in range(10):
    for y in range(20):
        i = 0
        if random() > .5:
            i = 1
        pop[x].append(i)


def control(countdown):
    while countdown != 0 and not term:
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


def selection(popSelect):
    rand = random() * 10
    return popSelect[int(rand)]


def crossover(father, mother):
    first = []
    last = []
    for j in range(5):
        first.append(mother[j])
        last.append(father[j])
    for j in range(5, 10):
        last.append(mother[j])
        last.append(father[j])
    return father, mother


def mutate(ind):
    for i in ind:
        if random() < .1:
            if ind[i] == 0:
                ind[i] = 1
            else:
                ind[i] = 0
    return ind


def elitism(p, np):
    global best
    for n in p:
        q = 0
        if sum(p) > q:
            best = p
    np.append(best)
    return np


def main():
    countdown = 10
    control(countdown)


main()
