from geneticalgorithm.initiation import Initiation
from geneticalgorithm import Population

from tree.random import randomTree
from tree import checkdomain

class TreeRandomInitiation(Initiation, object):
    def __init__(self, trainSet):
        self.trainSet = trainSet

    def __call__(self, Np):
        super(TreeRandomInitiation, self).__call__(Np)

        population = Population()

        for i in range(0, Np):
            tree = randomTree()
            while not checkdomain(tree, self.trainSet):
                tree = randomTree()

            population.append(tree)

        return population



