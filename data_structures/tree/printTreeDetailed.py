from implementationoftreenode import TreeNode

# we handle root and let recursion take care of everything else

root =TreeNode(1)

child1=TreeNode(2)
child2=TreeNode(3)
child3=TreeNode(4)

root.children.append(child1)
child1.children.append(child2)
root.children.append(child3)

def printTreeDetailed(root):
    if root==None:
        return
    
    print(root.data, end=":")
    
    for eachChild in root.children:
        print(eachChild.data,end=",")

    print()

    for eachChild in root.children:
        printTreeDetailed(eachChild)

# printTreeDetailed(root)