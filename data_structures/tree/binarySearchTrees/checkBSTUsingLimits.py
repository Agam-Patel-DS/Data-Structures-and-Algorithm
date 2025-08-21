from binarySearchTree import BSTNode, printBinarySearchTree, root, print_bst


def checkBSTUsingRange(root, mini, maxi):
    if root == None:
        return True
    
    if root.data<mini or root.data>maxi:
        return False
    
    ansLeft=checkBSTUsingRange(root.left, mini, root.data-1)
    ansRight=checkBSTUsingRange(root.right, root.data+1, maxi)

    return ansLeft and ansRight


print(checkBSTUsingRange(root, float("-inf"), float("inf")))
