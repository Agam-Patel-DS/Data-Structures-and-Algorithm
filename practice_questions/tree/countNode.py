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
root.children.append(child3)
root.children.append(child4)
root.children.append(child5)
root.children.append(child6)

def countNodes(root):
    if root==None:
        return
    
    childNodes=len(root.children)
    # print(f"The total child nodes of root {root.data} are {childNodes}")
    total_nodes=1
    for child in root.children:
        total_nodes=total_nodes+countNodes(child)-1
        # print(f"The total nodes below the node {root.data} are {total_nodes}")

    return total_nodes+childNodes

def countNodeSecond(root):
    if root==None:
        return 0
    numberOfNodes=1
    for eachChild in root.children:
        numberOfNodes=numberOfNodes+countNodeSecond(eachChild)

    return numberOfNodes

print(countNodes(root))
printTreeDetailed(root)
    




