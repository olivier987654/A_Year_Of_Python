## Python Script to create a reversed a binary tree

# A binary tree is a tree data structure in which each node has at most two children, which are referred to as the left child and the right child.


# Creating a class for the binary tree

class Node: # Creating a class for the node
    def __init__(self, val): # Creating a constructor for the node
        self.left = None # Creating a left node
        self.right = None # Creating a right node
        self.val = val # Creating a value for the node

# Creating a function to insert the nodes in the binary tree

def insert(root, node): # Creating a function to insert the nodes in the binary tree
    if root is None:
        root = node
    else:
        if root.val < node.val:
            if root.right is None:
                root.right = node
            else:
                insert(root.right, node)
        else:
            if root.left is None:
                root.left = node
            else:
                insert(root.left, node)

# Creating a function to print the binary tree

def printTree(root):
    if root:
        printTree(root.left)
        print(root.val)
        printTree(root.right)

