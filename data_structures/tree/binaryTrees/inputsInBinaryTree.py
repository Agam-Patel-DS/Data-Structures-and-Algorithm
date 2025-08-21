from introductionAndImplementation import BinaryTree
from printbinaryTree import printBinaryTree
from collections import deque

def takeBinaryTreeInput():

    data=int(input(f"Enter the input for node: "))
    if(data==-1):
        return None
    
    node=BinaryTree(data)
    print(f"Enter the left child of {data}")
    node.left=takeBinaryTreeInput()
    print(f"Enter the right child of {data}")
    node.right=takeBinaryTreeInput()

    return node

# node=takeBinaryTreeInput()
# printBinaryTree(node)

def inputLevelwise():
    data=int(input(f"Enter the input for root: "))
    if(data==-1):
        return None
    
    root=BinaryTree(data)
    queue=deque([root])
    while len(queue)!=0:
        currentNode=queue.popleft()
        leftChildData=int(input(f"Enter the left child for {currentNode.data} "))
        if leftChildData!=-1:
            leftNode=BinaryTree(leftChildData)
            currentNode.left=leftNode
            queue.append(leftNode)
        rightChildData=int(input(f"Enter the right child for {currentNode.data} "))
        if rightChildData!=-1:
            rightNode=BinaryTree(rightChildData)
            currentNode.right=rightNode
            queue.append(rightNode)

    return root


# node=inputLevelwise()
# printBinaryTree(node)