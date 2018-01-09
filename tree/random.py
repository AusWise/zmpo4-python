from __future__ import absolute_import

from tree import Tree
from tree.node import NodeType
from tree.node import Constant
from tree.node import Variable
from tree.node import node_factory

import random

maxDepth = 5
minConst = 0
maxConst = 100

def randomTree():
    return Tree(randomTreePart())

def randomTreePart(depth=maxDepth):
    if(depth==0):
        return randomLeaf()

    choose = random.randint(0, 5)
    if(choose in [NodeType.VAR, NodeType.CONST]):
        return randomLeaf(choose)
    else:
        return randomNode(depth, choose)

def randomNode(depth=maxDepth, choose=None):
    if choose==None:
        choose = random.randint(2, 5)

    return node_factory[choose](randomTreePart(depth - 1), randomTreePart(depth - 1))

def randomLeaf(choose=None):
    if choose==None:
        choose = random.randint(0, 1)

    if (choose == NodeType.CONST):
        value = random.randint(minConst, maxConst)
        return Constant(value)
    elif (choose == NodeType.VAR):
        return Variable(
            {
                0: 'x',
                1: 'y'
            }[random.randint(0, 1)]
        )
    else:
        assert False