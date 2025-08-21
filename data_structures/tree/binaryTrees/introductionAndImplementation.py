# Subset of generic tree, with a condtion that --->
# Speacialized kind of generic-tree which can have at most two children.

# more simpler than generic tree
# extremely useful for various computational purposes

# Use - Yes/No decision making, family tree with two parents
# Industry - Binary Decision Tree(ML), Database searching, Compilers(Abstract syntax tree)

# BinaryTreeNode - leftChild, rightChild, data

# Each of left, right node is a binary tree itself. 
#     
#    1        1
#   / \  !=  /  \
#  2   3    3    2
# (left)    (right)

class BinaryTree:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


root = BinaryTree(1)
root.left=BinaryTree(2)
root.right=BinaryTree(3)

