# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/6063963074854912

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from utils import TreeNode

def lowest_common_ancestor(root, node1, node2):
    # The official solution follows an iterative approach to traversing 
    # the nodes as opposed to the recursive approach done here, which 
    # might be better as we avoid consuming call stack space for the
    # recursive calls.
    
    if root.data > node1.data and \
       root.data > node2.data:
        return lowest_common_ancestor(root.left, node1, node2)
    
    if root.data < node1.data and \
       root.data < node2.data:
        return lowest_common_ancestor(root.right, node1, node2)

    return root