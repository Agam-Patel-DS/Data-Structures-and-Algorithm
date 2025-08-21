from implementationoftreenode import TreeNode
from printTreeDetailed import printTreeDetailed
from collections import deque
# Breadth first or level wise input



def takeInputBetter():
    data=int(input("Enter the data of the root: "))

    root=TreeNode(data)

    queue=deque([root])

    while (len(queue))!=0:
        currentNode=queue.popleft()
        numChildren=int(input("Enter the number of children for "+str(currentNode.data)+" "))
        for i in range(numChildren):
            child_data=int(input(f"Enter the data for child {i+1} of the current node: "))
            child_node=TreeNode(child_data)
            currentNode.children.append(child_node)
            queue.append(child_node)
    return root




root=takeInputBetter()
printTreeDetailed(root)