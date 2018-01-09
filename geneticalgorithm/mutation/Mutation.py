import random
import math
import copy

class Mutation:
    def __call__(self, population, p):
        for individual in population:
            if random.random() < p:
                population.append(self._mutate(individual))

        return population

    def _mutate(self, individual):
        child = copy.deepcopy(individual)
        n = random.randint(0, child.m-1)
        # print child, child[n], math.fabs(child[n]-1)
        child[n] = math.fabs(child[n]-1)
        return child