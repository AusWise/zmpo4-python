from geneticalgorithm.mutation import Mutation
from tree.random import randomLeaf
from tree.random import randomNode
from tree import checkdomain

import random

class TreeMutationStrategy:
    def __call__(self, tree):
        pass

import copy

class LeafToLeaf(TreeMutationStrategy):
    def __call__(self, tree):
        child = copy.deepcopy(tree)
        traversed = child.traverse()
        leafs = filter(lambda node: node.isLeaf(), traversed)
        leaf = random.choice(leafs)
        parent = leaf.parent
        i = leaf.i
        newLeaf = randomLeaf()
        if not parent:
            child.root = newLeaf
        else:
            parent[i] = newLeaf

        return newLeaf

class LeafToNode(TreeMutationStrategy):
    def __call__(self, tree):
        child = copy.deepcopy(tree)
        traversed = child.traverse()
        leafs = filter(lambda node: node.isLeaf(), traversed)
        leaf = random.choice(leafs)
        parent = leaf.parent
        i = leaf.i
        newNode = randomNode()
        if not parent:
            child.root = newNode
        else:
            parent[i] = newNode

        return newNode

class NodeToLeaf(TreeMutationStrategy):
    def __call__(self, tree):
        child = copy.deepcopy(tree)
        traversed = child.traverse()
        nodes = filter(lambda node: not node.isLeaf(), traversed)
        if not nodes:
            return None

        node = random.choice(nodes)
        parent = node.parent
        i = node.i
        newLeaf = randomLeaf()
        if not parent:
            child.root = newLeaf
        else:
            parent[i] = newLeaf

        return newLeaf

class NodeToNode(TreeMutationStrategy):
    def __call__(self, tree):
        child = copy.deepcopy(tree)
        traversed = child.traverse()
        nodes = filter(lambda node: not node.isLeaf(), traversed)
        if not nodes:
            return None

        node = random.choice(nodes)
        parent = node.parent
        i = node.i
        newNode = randomNode()
        if not parent:
            child.root = newNode
        else:
            parent[i] = newNode

        return child

# class TreeMutationStrategyEnum(Enum):
#     LEAF_TO_LEAF = 0,
#     LEAF_TO_NODE = 1,
#     NODE_TO_LEAF = 2,
#     NODE_TO_NODE = 3

mutationStrategy = [
    LeafToLeaf(),
    LeafToNode(),
    NodeToLeaf(),
    NodeToNode()
]

class TreeMutation(Mutation):
    def __init__(self, trainSet):
        self.trainSet = trainSet

    def _mutate(self, tree):
        choose = random.randint(0,3)
        child = mutationStrategy[choose](tree)

        while child == None or not checkdomain(child, self.trainSet):
            choose = random.randint(0, 3)
            child = mutationStrategy[choose](tree)

        return child


