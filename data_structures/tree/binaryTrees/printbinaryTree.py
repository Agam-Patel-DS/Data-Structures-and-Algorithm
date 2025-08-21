from introductionAndImplementation import BinaryTree

root=BinaryTree(1)
root.left=BinaryTree(2)
root.right=BinaryTree(3)
root.left.left=BinaryTree(4)
root.right.right=BinaryTree(5)

def printBinaryTree(root):

    if root==None: # in generic tree this was edge case, here it is base case
        return
    
    print(root.data, end=":")
    if root.left!=None:
        print(f"L->{root.left.data}", end=",")
    else:
        print("L->None", end=",")
    
    if root.right!=None:
        print(f"R->{root.right.data}")
    else:
        print("R->None")

    printBinaryTree(root.left) #recursion
    printBinaryTree(root.right) #recursion


#printBinaryTree(root)