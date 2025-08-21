from sortedArrayListToBST import BSTNode, sortedArrayListToBST, root, printBinarySearchTree

# 1. Check with maximum value of left subtree
# 2. Minimum of the right subtree
# 3. Each and every subtree is also a BST

def findMax(root):
    if root is None:
        return float("-inf")
    
    leftMax=findMax(root.left)
    rightMax=findMax(root.right)

    ans = max(leftMax, rightMax, root.data)
    return ans

def findMin(root):
    if root is None:
        return float("inf")
    
    leftMin=findMin(root.left)
    rightMin=findMin(root.right)

    ans = min(leftMin, rightMin, root.data)
    return ans


def checkBST(root): # Time Complexity == O(nlogn) and O(n^2)
    if(root is None):
        return True  # Empty tree is a BST
    
    leftMax=findMax(root.left)
    rightMin=findMin(root.right)

    leftBST=checkBST(root.left)
    rightBST=checkBST(root.right)

    ans=leftBST and rightBST and (leftMax<root.data) and (root.data<rightMin)

    return ans

root1=sortedArrayListToBST([1,2,3,4,5,6,7,8,0])
printBinarySearchTree(root1)
print(checkBST(root1))
