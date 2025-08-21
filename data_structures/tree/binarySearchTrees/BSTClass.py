class BSTNode:
    def __init__(self, data):
        self.data=data
        self.left=None
        self.right=None


class BST:
    def __init__(self):
        self.root=None

    def insert(self, data): # O(height)
        self.insertHelper(self,data,self.root)

    def insertHelper(self,data,node):
        if node==None:
            newNode=BSTNode(data)
            return newNode
        
        if data<node.data:
            node.left=self.insertHelper(data,node.left)

        else:
            node.right=self.insertHelper(data,node.right)

    def search(self,data): # O(height)
        return self.searchHelper(data,self.root)

    def searchHelper(self, data, root):
        if (root==None):
            return False
        
        if root.data==data:
            return True
        
        if data<root.data:
            return self.searchHelper(data, root.left)
        else:
            return self.searchHelper(data,root.right)
        
    def getMinNode(self,node):
        current=node
        while(current.left!=None):
            current=current.left
        return current

    def deleteHelper(self,data,root):
        if root==None:
            return None

        if data<root.data:
            root.left=self.deleteHelper(data,root.left) #find left

        elif data>root.data:
            root.right=self.deleteHelper(data,root.right) #find right

        # if node is a leaf --> delete and return None
        # if node has either right or left child and one side is none. 
        # ----> return the left or right subtree of the node.
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
        # if left and right of the node are not None
        # ----> replace the node with the lowest of its right subtree
        # ----> replace the node with the greatest of its left subtree
            minLargerNode=self.getMinNode(root.right)
            root.data=minLargerNode.data
            #deleting the duplicate replaced node in the tree
            root.right=self.deleteHelper(minLargerNode.data,root.right) 

        return root

    def delete(self,data): # O(height)
        self.root=self.deleteHelper(data,self.root)


# just balance the tree and the complexty tunrs to O(logn) from O(height)

