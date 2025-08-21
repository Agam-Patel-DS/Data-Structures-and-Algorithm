class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]    

#inorder - left, root, right
#preorder - root, left, right


# in preorder, the first will always be the tree root

# ------ Example -------
# Preorder - 1,2,4,5,3,6

# Inorder - 4,2,5,1,3,6

# Postorder - 4,5,2,6,3,1

# constructTree(inorder, preorder, inS, inE, prS, prE)

# root -> preorder[0]
# left-> linS=inS, linE=inRI, lprS=prS+1, lprE=(linE-linS+lprS) (inRI: Inorder Root Index)
# right-> rInS=(rprS-rprE)+rinE, rinE=inE, rprS=lprE+1, rprE=prE

def constructFromInOrderPreOrder():
    pass