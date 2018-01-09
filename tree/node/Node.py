class Node:
    def __init__(self, parent=None, i=-1):
        self.parent = parent
        self.i = i
        self.children = []

    def __call__(self, *args, **kwargs):
        pass

    def __str__(self):
        pass

    def __iter__(self):
        return iter(self.children)

    def __getitem__(self, i):
        return  self.children[i]

    def __setitem__(self, i, node):
        node.parent = self
        node.i = i
        if i >= len(self.children):
            self.children.append(node)
        else:
            self.children[i] = node

    def isLeaf(self):
        return not self.children

    def traverse(self):
        traversed = []
        for node in self:
            traversed.extend(node.traverse())

        traversed.append(self)
        return traversed

class Variable(Node, object):
    def __init__(self, name):
        Node.__init__(self)
        self.name = name

    def __call__(self, *args, **kwargs):
        Node.__call__(self, *args, **kwargs)
        return kwargs[self.name]

    def __str__(self):
        super(Variable, self).__str__()
        return self.name

class Constant(Node, object):
    def __init__(self, value=0):
        Node.__init__(self)
        self.value = value

    def __call__(self, *args, **kwargs):
        Node.__call__(self, *args, **kwargs)
        return self.value

    def __str__(self):
        super(Constant, self).__str__()
        return str(self.value)

class BinaryOperation(Node, object):
    def __init__(self, left, right):
        Node.__init__(self)
        self.left = left
        self.right = right

    @property
    def left(self):
        return self[0]

    @left.setter
    def left(self, node):
        self[0] = node

    @property
    def right(self):
        return self[1]

    @right.setter
    def right(self, node):
        self[1] = node

class Add(BinaryOperation):
    def __init__(self, left, right):
        super(Add, self).__init__(left, right)

    def __call__(self, *args, **kwargs):
        super(Add, self).__call__(*args, **kwargs)
        return self.left(*args, **kwargs) + self.right(*args, **kwargs)

    def __str__(self):
        super(Add, self).__str__()
        return '(' + str(self.left) + '+' + str(self.right) + ')'

class Sub(BinaryOperation):
    def __init__(self, left, right):
        super(Sub, self).__init__(left, right)

    def __call__(self, *args, **kwargs):
        super(Sub, self).__call__(*args, **kwargs)
        return self.left(*args, **kwargs) - self.right(*args, **kwargs)

    def __str__(self):
        super(Sub, self).__str__()
        return '(' + str(self.left) + '-' + str(self.right) + ')'

class Multiply(BinaryOperation):
    def __init__(self, left, right):
        super(Multiply, self).__init__(left, right)

    def __call__(self, *args, **kwargs):
        super(Multiply, self).__call__(*args, **kwargs)
        return self.left(*args, **kwargs) * self.right(*args, **kwargs)

    def __str__(self):
        super(Multiply, self).__str__()
        return '(' + str(self.left) + '*' + str(self.right) + ')'


class Divide(BinaryOperation):
    def __init__(self, left, right):
        super(Divide, self).__init__(left,right)

    def __call__(self, *args, **kwargs):
        super(Divide, self).__call__(self, *args, **kwargs)
        return self.left(*args, **kwargs) / self.right(*args, **kwargs)

    def __str__(self):
        super(Divide, self).__str__()
        return '(' + str(self.left) + '/' + str(self.right) + ')'

from enum import Enum

class NodeType(Enum):
    CONST = 0
    VAR = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5

node_factory = {
    2 : Add,
    3 : Sub,
    4 : Multiply,
    5 : Divide,
}