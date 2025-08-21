class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]    

#inorder - left, root, right
#preorder - root, left, right
#postorder - left, right, root

# in preorder, the first will always be the tree root

# ------ Example -------
# Preorder - 1,2,4,5,3,6

# Inorder - 4,2,5,1,3,6

# Postorder - 4,5,2,6,3,1

# constructTree(inorder, postorder, inS, inE, poS, poE)
# inRI: Inorder Root Index

# root -> postorder[n-1]
# left -> linS=inS, linE=inrI-1, lpoS=poS, lpoE=(linE-linS)+lpoS
# right -> rinS=inRI+1, rinE=inE, rpoS=lpoE+1, rpoE=poE-1


def constructFromInOrderPostOrder():
    pass