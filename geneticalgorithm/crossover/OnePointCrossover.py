from . import Crossover
from .. import Individual

import random

class OnePointCrossover(Crossover, object):
    def _crossover(self, parent1, parent2):
        m = parent1.m
        v = parent1.v

        crossPoint = random.randint(0, m-1)

        child1 = Individual(m, v)
        child2 = Individual(m, v)

        for i in range(0, crossPoint):
            child1[i] = parent1[i]
            child2[i] = parent2[i]

        for i in range(crossPoint, m):
            child1[i] = parent2[i]
            child2[i] = parent1[i]

        return (child1, child2)