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

root1 =TreeNode(1)

child1=TreeNode(2)
child2=TreeNode(3)
child3=TreeNode(4)
child4=TreeNode(5)
child5=TreeNode(6)
child6=TreeNode(7)

root1.children.append(child1)
root1.children.append(child2)
root1.children.append(child3)
root1.children.append(child4)
root1.children.append(child5)
root1.children.append(child6)

root2 =TreeNode(11)

child1=TreeNode(22)
child2=TreeNode(33)
child3=TreeNode(44)
child4=TreeNode(55)
child5=TreeNode(66)
child6=TreeNode(77)

root2.children.append(child1)
child1.children.append(child2)
root2.children.append(child3)
child2.children.append(child4)
child4.children.append(child5)
root2.children.append(child6)


def preorderTraversal(root):
    if root == None:
        return
    print(root.data, end=" ") # first root then children
    for eachChild in root.children:
        preorderTraversal(eachChild)

print("Preorder Traversal: ")
printTreeDetailed(root2)
preorderTraversal(root2)

def postorderTraversal(root):
    if root == None:
        return
    for eachChild in root.children: # first children then the root
        postorderTraversal(eachChild)

    print(root.data, end=" ")

print("\nPostorder Traversal: ")
printTreeDetailed(root2)
postorderTraversal(root2)
