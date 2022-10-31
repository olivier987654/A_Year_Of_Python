## Binary trees in Python 3

class Node: # A node in a binary tree has a value and two children
    def __init__(self, value): # Constructor
        self.value = value # Value of the node
        self.left = None # Left child
        self.right = None # Right child

    def __str__(self): # String representation of a node
        return str(self.value) # Just return the value

    # Insert a new node into the tree rooted at this node

    def insert(self, value): # Insert a new node with value
        if value < self.value: # If value is less than this node's value
            if self.left is None: # If there is no left child
                self.left = Node(value) # Create a new node
            else: # If there is a left child
                self.left.insert(value) # Insert into the left subtree

# A binary tree is a node with a root node and a size (number of nodes), it is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner. It is a non-linear data structure and is used to store data in a tree-like structure. It is a data structure that is used to store data in a hierarchical manner
