from geneticalgorithm import GeneticAlgorithm
from tree.geneticalgorithm import TreeFitnessFunction
from geneticalgorithm.selection import TournamentSelection
from tree.geneticalgorithm import TreeCrossover
from tree.geneticalgorithm import TreeMutation
from tree.geneticalgorithm import TreeRandomInitiation

class TreeGeneticAlgorithm(GeneticAlgorithm, object):
    def __init__(self, Np, Ni, Pk, Pm, trainSet):
        super(TreeGeneticAlgorithm, self).__init__(Np=Np,
                                                   Ni=Ni,
                                                   Pk=Pk,
                                                   Pm=Pm,
                                                   initiation=TreeRandomInitiation(trainSet),
                                                   fitness=TreeFitnessFunction(trainSet),
                                                   selection=TournamentSelection(3),
                                                   crossover=TreeCrossover(trainSet),
                                                   mutation=TreeMutation(trainSet)
                                                   )
