from implementationoftreenode import TreeNode

# we handle root and let recursion take care of everything else

root =TreeNode(1)

child1=TreeNode(2)
child2=TreeNode(3)
child3=TreeNode(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

def printTree(root):
    print(root.data)
    for eachChild in root.children:
        printTree(eachChild)

printTree(root)