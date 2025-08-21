class BSTNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def searchBST(root, value):
    if root==None:
        print("Reached Dead End")
        return False
    if root.data==value:
        print(f"Found the {value} in the tree.")
        return True
    
    if root.data>value:
        print(f"Not this root({root.data}), going left.")
        return searchBST(root.left, value)
    else:
        print(f"Not this root({root.data}), going right.")
        return searchBST(root.right, value)
       

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

print(searchBST(root, 11))