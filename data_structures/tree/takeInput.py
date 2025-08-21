from implementationoftreenode import TreeNode
from printTreeDetailed import printTreeDetailed
# we handle root and let recursion take care of everything else

# This is height first input

def initialiseTreeNode():
    data=int(input("Enter the data: "))
    node=TreeNode(data)
    numChildren=int(input(f"Number of children for {data}: "))
    for eachChild in range(numChildren):
        child=initialiseTreeNode()
        node.children.append(child)
    return node

root=initialiseTreeNode()

printTreeDetailed(root)