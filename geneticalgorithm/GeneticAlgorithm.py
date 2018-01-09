from fitnessfunction.FitnessFunction import decimal

class GeneticAlgorithm:
    def __init__(self, initiation, Np, Ni, fitness, selection,crossover, Pk, mutation, Pm):
        self.initiation = initiation
        self.population = None
        self.Np = Np
        self.Ni = Ni
        self.fitness = fitness
        self.selection = selection
        self.crossover = crossover
        self.Pk = Pk
        self.mutation = mutation
        self.Pm = Pm

    def __call__(self, *args, **kwargs):
        self.population = self.initiation(self.Np)

        self.evaluate()

        for t in range(self.Ni):
            print t,  self.population.best.fitness, self.population.avgFitness, self.population.worst.fitness, str(self.population.best)
            self.population = self.selection(self.population, self.Np)
            self.crossover(self.population, self.Pk)
            self.mutation(self.population, self.Pm)
            self.evaluate()

    def evaluate(self):
        for individual in self.population:
            individual.fitness = self.fitness(individual)



