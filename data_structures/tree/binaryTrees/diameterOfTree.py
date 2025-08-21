# Diameter - maximum distance between two points in the cicle
# Diameter of Tree - the maximum distance between any two nodes in a tree

#     1
#   /  \
#  2    3 The diameter is 2 ( 2 --> 1 --> 3 (2 and 3 counted))

# Diameter = lmaximum(leftHeight-rightHeight, leftDiameter, rightDiameter)
# Diameter can consist of nodes not passing through root


from introductionAndImplementation import BinaryTree
from printbinaryTree import printBinaryTree
from inputsInBinaryTree import inputLevelwise

def height(root): # O(n) Complexity
    if root==None:
        return 0

    leftHeight=height(root.left)
    rightHeight=height(root.right)

    heightOfTree=1+max(leftHeight, rightHeight)

    return heightOfTree

def diameterOfTree(root):
    if root==None:
        return 0

    lefHeight=height(root.left)
    rightHeight=height(root.right)

    leftDiameter=diameterOfTree(root.left)
    rightDiameter=diameterOfTree(root.right)

    ans=max(leftDiameter, rightDiameter, lefHeight+rightHeight)

    return ans

# root=inputLevelwise()
# printBinaryTree(root)
# print(f"The diameter of the tree is {diameterOfTree(root)}")

# The overall complexity - O(n*h) where n - number of nodes, h - height of the tree

def diameterOptimised(root):
    if root==None:
        return 0,0 #height, diameter
    
    leftHeight, leftDiameter=diameterOptimised(root.left)
    rightHeight, rightDiameter=diameterOptimised(root.right)

    diameterThroughRoot=leftHeight+rightHeight
    
    ansDiameter=max(diameterThroughRoot, leftDiameter, rightDiameter)
    currentTreeHeight=1+max(leftHeight, rightHeight)
    return currentTreeHeight, ansDiameter



root=inputLevelwise()
printBinaryTree(root)
heightOfTree, diameter=diameterOptimised(root)
print(f"The diameter of the tree is {diameter} and height is {heightOfTree}")