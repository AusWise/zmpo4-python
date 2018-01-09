from Tree import Tree

def checkdomain(tree, train_set):
    try:
        for (x,y,_) in train_set:
            tree(x=x,y=y)
        return True
    except ZeroDivisionError:
        return False
