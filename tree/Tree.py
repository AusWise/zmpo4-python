from tree.node import Node

class Tree:
    def __init__(self, root=None):
        if root!=None:
            self.root = root
        else:
            self.root = Node()

    def __call__(self, *args, **kwargs):
        return self.root(*args, **kwargs)

    def __str__(self):
        return str(self.root)


    def traverse(self):
        return self.root.traverse()
