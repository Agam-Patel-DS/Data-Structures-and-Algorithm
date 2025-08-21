from binarySearchTree import printBinarySearchTree
class BSTNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

sample_array=[1,2,3,4,5,6,7,8,9,10]

def sortedArrayListToBST(array):
    if len(array)==0:
        return None

    mid=len(array)//2
    rootData=array[mid]
    root=BSTNode(rootData)
    
    root.left=sortedArrayListToBST(array[:mid])
    root.right=sortedArrayListToBST(array[mid+1:])
    return root

    

e=len(sample_array)
root=sortedArrayListToBST(sample_array)
# printBinarySearchTree(root)
