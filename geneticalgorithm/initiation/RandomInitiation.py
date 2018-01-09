from . import Initiation
from .. import Population
from .. import Individual

import random

class RandomInitiation(Initiation, object):
    def __init__(self, m, v):
        self.m = m
        self.v = v

    def __call__(self, Np):
        super(RandomInitiation, self).__call__(Np)

        population = Population()
        for i in range(Np):
            individual = Individual(self.m, self.v)

            for j in range(self.m):
                individual[j] = random.randint(0, self.v-1)

            population.append(individual)

        return population


