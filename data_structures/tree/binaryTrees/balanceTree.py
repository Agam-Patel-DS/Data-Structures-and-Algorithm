from introductionAndImplementation import BinaryTree
from printbinaryTree import printBinaryTree
from inputsInBinaryTree import inputLevelwise

# Balanced Tree - If at each node, leftHeight-rightHeight <=1 
# Then the tree is height balanced.


def isBalanced(root):
    pass


root=inputLevelwise()
printBinaryTree(root)
result=isBalanced(root)
if result:
    print(f"The tree is balanced")
else:
    print("Unbalanced Tree")