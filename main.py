# import random
# from enum import Enum
# from collections import OrderedDict
# import copy
#
#
#
#
# maxDepth = 5
# minConst = 0
# maxConst = 100
#
# Np = 1000
# Ni = 100
# Pk = 0.7
# Pm = 0.1
#
# def randomTree():
#     return Tree(randomTreePart())
#
# def randomTreePart(depth=maxDepth):
#     if(depth==0):
#         return randomLeaf()
#
#     choose = random.randint(0, 5)
#     if(choose in [NodeType.VAR, NodeType.CONST]):
#         return randomLeaf(choose)
#     else:
#         return randomNode(depth, choose)
#
# def randomNode(depth=maxDepth, choose=None):
#     if choose==None:
#         choose = random.randint(2, 5)
#
#     return node_factory[choose](randomTreePart(depth - 1), randomTreePart(depth - 1))
#
# def randomLeaf(choose=None):
#     if choose==None:
#         choose = random.randint(0, 1)
#
#     if (choose == NodeType.CONST):
#         value = random.randint(minConst, maxConst)
#         return Constant(value)
#     elif (choose == NodeType.VAR):
#         return Variable(
#             {
#                 0: 'x',
#                 1: 'y'
#             }[random.randint(0, 1)]
#         )
#     else:
#         assert False
#
# def checkdomain(tree, train_set):
#     try:
#         for (x,y,_) in train_set:
#             tree(x=x,y=y)
#         return True
#     except ZeroDivisionError:
#         return False
#
# def init(train_set ,Np = Np):
#     population = []
#
#     for i in range(0, Np):
#         tree = randomTree()
#         while not checkdomain(tree, train_set):
#             tree = randomTree()
#
#         population.append(tree)
#
#     return population
#
# def select(population, error):
#     new_population = []
#     for i in range(Np):
#         pair = (random.choice(population), random.choice(population))
#         tree = min(pair, key=lambda x: error[x])
#         # print tree
#         population.remove(tree)
#         new_population.append(tree)
#
#     return new_population
#
# def cross():
#     pass
#
# def crossTrees(parent1, parent2):
#     child1 = copy.deepcopy(parent1)
#     child2 = copy.deepcopy(parent2)
#
#     traversed1 = child1.traverse()
#     traversed2 = child2.traverse()
#
#     (node1, parentNode1, i1) = random.choice(traversed1)
#     (node2, parentNode2, i2) = random.choice(traversed2)
#
#     parentNode1
#
# class MutationStrategy(Enum):
#     LEAF_TO_LEAF = 0,
#     LEAF_TO_NODE = 1,
#     NODE_TO_LEAF = 2,
#     NODE_TO_NODE = 3
#
# def mutate(population, train_set):
#     childs = []
#     for tree in population:
#         if(random.random()<Pm):
#             child = mutateTree(tree)
#
#             while child==None or not checkdomain(child, train_set):
#                 child = mutateTree(tree)
#
#             childs.append(child)
#
#     population.extend(childs)
#
# def mutateTree(tree):
#     choose = random.randint(0, 3)
#     child = copy.deepcopy(tree)
#     traversed = child.traverse()
#     if (choose == MutationStrategy.LEAF_TO_LEAF):
#         leafs = filter(lambda node: node.isLeaf(), traversed)
#         leaf = random.choice(leafs)
#         parent = leaf.parent
#         i = leaf.i
#         newLeaf = randomLeaf()
#         if not parent:
#             child.root = newLeaf
#         else:
#             parent[i] = newLeaf
#
#     elif (choose == MutationStrategy.LEAF_TO_NODE):
#         leafs = filter(lambda node: node.isLeaf(), traversed)
#         leaf = random.choice(leafs)
#         parent = leaf.parent
#         i = leaf.i
#         newNode = randomNode()
#         if not parent:
#             child.root = newNode
#         else:
#             parent[i] = newNode
#
#     elif (choose == MutationStrategy.NODE_TO_LEAF):
#         nodes = filter(lambda node: not node.isLeaf(), traversed)
#         if not nodes:
#             return None
#
#         node = random.choice(nodes)
#         parent = node.parent
#         i = node.i
#         newLeaf = randomLeaf()
#         if not parent:
#             child.root = newLeaf
#         else:
#             parent[i] = newLeaf
#
#     elif (choose == MutationStrategy.NODE_TO_NODE):
#         nodes = filter(lambda node: not node.isLeaf(), traversed)
#         if not nodes:
#             return None
#
#         node = random.choice(nodes)
#         parent = node.parent
#         i = node.i
#         newNode = randomNode()
#         if not parent:
#             child.root = newNode
#         else:
#             parent[i] = newNode
#
#     return child
#
# def eval(train_set, tree):
#     if(isinstance(tree, Tree)):
#         error = 0
#         for (x,y,z) in train_set:
#             error += (z-tree(x=x, y=y)) ** 2
#
#         return error
#
#     else:
#         population = tree
#         error = {}
#         for tree in population:
#             error[tree] = eval(train_set, tree)
#
#         return error
#
def parse(filename):
    f = open(filename, 'r')
    train_set = []
    for line in f:
        strs = line.split()
        x = float(strs[0][:-1])
        y = float(strs[1][:-1])
        z = float(strs[2][:-1])
        train_set.append((x,y,z))

    return train_set
#
# def test(filename):
#     train_set = parse(filename)
#
#     population = init(train_set)
#     error = eval(train_set, population)
#
#     for i in range(Ni):
#         population = select(population, error)
#
#         mutate(population, train_set)
#
#         error = eval(train_set, population)
#
#     print filename
#     for tree in error.keys():
#         print error[tree], tree
#
#     print ""
#
# test("ZMPO_lista_4_00_punkt.txt")
# test("ZMPO_lista_4_01_2_punkty.txt")
# test("ZMPO_lista_4_02_3_punkty.txt")
# test("ZMPO_lista_4_03_sin_x.txt")
# test("ZMPO_lista_4_04_sin_x_y.txt")
# test("ZMPO_lista_4_05_x_y_pl_x_x.txt")
# test("ZMPO_lista_4_06_x_y_pl_x_x_noise.txt")
#
# def PG():
#     pass
#
#

# from geneticalgorithm import GeneticAlgorithm
# from geneticalgorithm.initiation import RandomInitiation
# from geneticalgorithm.selection import TournamentSelection
# from geneticalgorithm.crossover import OnePointCrossover
# from geneticalgorithm.mutation import Mutation
# from geneticalgorithm.fitnessfunction import FitnessFunction
from tree.geneticalgorithm import TreeGeneticAlgorithm

# f1 = lambda x: -(x-3) ** 2 + 1
# f2 = lambda x: -(x-1)*(x-3)*(x-4)*(x-6)*x

# initiation = RandomInitiation(3, 2)
# selection = TournamentSelection(3)
# mutation = Mutation()
# crossover = OnePointCrossover()
# fitnessFunction = FitnessFunction(f2)
#geneticAlgorithm = GeneticAlgorithm(initiation, 10, 100 , fitnessFunction, selection, crossover, 0.7, mutation, 0.1)

def test(filename):
    trainSet = parse(filename)
    geneticAlgorithm = TreeGeneticAlgorithm(100, 10, 0.7, 0.1, trainSet)
    geneticAlgorithm()

test("ZMPO_lista_4_03_sin_x.txt")