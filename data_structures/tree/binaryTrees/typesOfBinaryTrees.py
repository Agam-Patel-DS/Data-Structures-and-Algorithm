# =======================================================
# Types of Binary Trees
# =======================================================

# -------------------------------------------------------
## 1. On basis of number of children 
# -------------------------------------------------------
### A. Full Binary Tree -> Every parent/internal nodes has either 2 or no children
### B. Degenerate Binary Tree -> Only one child, either right or left. 
### C. Skewed Binary Tree -> Either only left children or only right children.

# -------------------------------------------------------
## 2. On the basis of completion of level 
# -------------------------------------------------------
### A. Complete Binary Tree -> All level completely filled except, 
#     last level have nodes as to the last as possible.
### B. Perfect Binary Tree -> Every node has two children and 
#     all leaf nodes are at the same level. (completely filled)
#     - Number of leat nodes = 1+internal nodes
#     - Number of nodes in each level = (2^(h+1))-1; h: height
### C. Balanced Binary Tree -> leftHeight-rightHeight in every 
#     node is less than or equals to 1.

# =======================================================
# Binary Search Tree
# =======================================================
## 1. On the left of the root, everything will be less than the root.
## 2. On the right of the root, everything will be greater than the root. 
## 3. Left and right subtree should also follow BST property. 