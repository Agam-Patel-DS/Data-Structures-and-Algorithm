def printTreeDetailed(root):
    if root==None:
        return
    
    print(root.data, end=":")
    
    for eachChild in root.children:
        print(eachChild.data,end=",")

    print()

    for eachChild in root.children:
        printTreeDetailed(eachChild)

class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]        

root =TreeNode(1)

child1=TreeNode(2)
child2=TreeNode(3)
child3=TreeNode(4)
child4=TreeNode(5)
child5=TreeNode(6)
child6=TreeNode(7)

root.children.append(child1)
root.children.append(child2)
child1.children.append(child3)
root.children.append(child4)
child3.children.append(child5)
root.children.append(child6)


def heightOfTree(root):
    if root == None:
        return 0 
    
    height=1
    maxChildHeight=0
    for eachChild in root.children:
        maxChildHeight=max(maxChildHeight,heightOfTree(eachChild))

    height=height+maxChildHeight
    return height

printTreeDetailed(root)
print(heightOfTree(root))