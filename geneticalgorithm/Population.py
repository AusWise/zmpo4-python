

class Population(list):

    @property
    def best(self):
        return max(self, key=lambda x: x.fitness)

    @property
    def avgFitness(self):
        _sum = sum(map(lambda x: x.fitness, self))
        return _sum/len(self)

    @property
    def worst(self):
        return min(self, key=lambda x: x.fitness)
