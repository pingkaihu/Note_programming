# Initiate the class of binary tree
class Tree(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


#   Three different ways to do depth first search (DFS) traversals

#   The rule of pre_order is root -> left -> right

def pre_order(node):

    if node:
        print(node.val)
        pre_order(node.left)
        pre_order(node.right)

    return node


#   The rule of pre_order is left-> root -> right

def in_order(node):

    if node:
        in_order(node.left)
        print(node.val)
        in_order(node.right)

    return node


#   The rule of pre_order is left -> right -> root

def post_order(node):

    if node:
        post_order(node.left)
        post_order(node.right)
        print(node.val)

    return node


# In order to realize the breadth first search, we need to have a queue

#def BFS_helper(node):
