import random

class Crossover:
    def __call__(self, population, p):
        for i in range(0, len(population), 2):
            if random.random()<p:
                childs = self._crossover(population[i], population[i+1])
                population.extend(childs)

    def _crossover(self, parent1, parent2):
        return []
