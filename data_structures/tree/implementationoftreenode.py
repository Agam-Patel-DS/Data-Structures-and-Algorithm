class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]

# Tree is a heirarchial data structure,
# consisting of nodes which are connected by edges.

root =TreeNode(1)

child1=TreeNode(2)
child2=TreeNode(3)
child3=TreeNode(4)

root.children.append(child1)
root.children.append(child2)
root.children.append(child3)

# print(root.children[0].data)