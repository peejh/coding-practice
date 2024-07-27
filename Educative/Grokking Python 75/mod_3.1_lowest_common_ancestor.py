# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/6063963074854912

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from utils import TreeNode

def lowest_common_ancestor(root, node1, node2):
    # This is a more generalized LCA function that also works 
    # for non-BST trees.
    # The approach is to find the paths to the nodes from root,
    # and return the first common parent of both nodes.
    
    path1 = find_node(root, node1, [])
    path2 = find_node(root, node2, [])

    # If either nodes does not exist in the tree
    if not path1 or not path2:
        return None

    # Traverse the paths from the nodes back to root and
    # return the first common parent for both
    for p1 in reversed(path1):
        for p2 in reversed(path2):
            if p1 == p2:
                return p1

def find_node(root, node, path):
    # Helper function for the LCA method.
    # Returns the path starting from root to the node as a list.
    
    # If node is not found in this branch
    if root is None:
        return False
    
    # If node is found
    if root == node:
        path.append(node)
        return path
    
    # Create a new list from current path to prevent using same
    # object reference on left and right branches
    root_path = path + [root]

    return find_node(root.left, node, root_path) \
        or find_node(root.right, node, root_path)