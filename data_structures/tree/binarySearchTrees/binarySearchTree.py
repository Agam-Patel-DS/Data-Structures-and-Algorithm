class BSTNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None



def print_bst(root):
    if(root is None):
        return
    print_bst(root.left)
    print(root.data, end=" ")
    print_bst(root.right)  # inorder traversal

def printBinarySearchTree(root):

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

    printBinarySearchTree(root.left) #recursion
    printBinarySearchTree(root.right) #recursion



root=BSTNode(7)
l1=BSTNode(5)
l2=BSTNode(4)
l3=BSTNode(6)
r1=BSTNode(9)
r2=BSTNode(8)
r3=BSTNode(10)

root.left=l1
root.right=r1
l1.left=l2
l1.right=l3
r1.left=r2
r1.right=r3

# print_bst(root)
# print()
# printBinarySearchTree(root)