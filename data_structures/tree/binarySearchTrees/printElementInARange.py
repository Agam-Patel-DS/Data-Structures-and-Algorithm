from binarySearchTree import BSTNode, printBinarySearchTree, root, print_bst

def printValuesInRange(root, low, high): # High Low Included
    if root==None:
        return
    
    if(low<root.data):
        printValuesInRange(root.left, low, high)

    if(low<=root.data<=high):
        print(root.data, end=" ")

    if(high>root.data):
        printValuesInRange(root.right, low, high)


# print_bst(root)
# print()
# printValuesInRange(root, 5, 9)