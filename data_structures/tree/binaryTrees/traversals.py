from introductionAndImplementation import BinaryTree
from printbinaryTree import printBinaryTree
from inputsInBinaryTree import inputLevelwise


# Preorder - first print parent, then children --> parent, left, right

def preOrder(root):
    if root==None:
        return 
    
    print(root.data, end=" ")
    preOrder(root.left)
    preOrder(root.right)

# root=inputLevelwise()
# print(f"The Pre-Order Traversal is: {preOrder(root)}")


# Postorder - first children, then parent --> left, right, parent

def postOrder(root):
    if root==None:
        return 
    
    postOrder(root.left)
    postOrder(root.right)
    print(root.data, end=" ")

# root=inputLevelwise()
# print(f"The Post-Order Traversal is:",end=" ")
# postOrder(root)

# Inorder - left, parent, right

def inOrder(root):
    if root==None:
        return 
    
    postOrder(root.left)
    print(root.data, end=" ")
    postOrder(root.right)

root=inputLevelwise()
print(f"The In-Order Traversal is:",end=" ")
inOrder(root)