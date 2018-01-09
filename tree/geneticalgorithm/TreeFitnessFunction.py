from geneticalgorithm.fitnessfunction import FitnessFunction

class TreeFitnessFunction(FitnessFunction):
    def __init__(self, trainSet):
        self.trainSet = trainSet

    def __call__(self, tree):
        return -sum(map(lambda (x, y, z): (z-tree(x=x,y=y))**2, self.trainSet))
