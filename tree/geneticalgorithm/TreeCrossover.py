from geneticalgorithm.crossover import Crossover

from tree import checkdomain

import random
import copy

class TreeCrossover(Crossover):
    def __init__(self, trainSet):
        self.trainSet = trainSet

    def _crossover(self, parent1, parent2):
        (child1, child2) = self.__crossover(parent1, parent2)
        while not checkdomain(child1, self.trainSet) or not checkdomain(child2, self.trainSet):
            (child1, child2) = self.__crossover(parent1, parent2)

        return (child1, child2)

    def __crossover(self, parent1, parent2):
        child1 = copy.deepcopy(parent1)
        child2 = copy.deepcopy(parent2)

        (splitNode1, i1, subTree1) = self._split(child1)
        (splitNode2, i2, subTree2) = self._split(child2)

        self._merge(child1, splitNode1, i1, subTree2)
        self._merge(child2, splitNode2, i2, subTree1)

        return (child1, child2)

    def _split(self, tree):
        traversed = tree.traverse()
        node = random.choice(traversed)
        parent = node.parent
        i = node.i

        return (parent, i, node)

    def _merge(self, tree, splitNode, i, subTree):
        if splitNode:
            splitNode[i] = subTree
        else:
            tree.root = subTree