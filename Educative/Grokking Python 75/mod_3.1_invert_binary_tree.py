# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/4875373087162368

from utils import TreeNode

def mirror_binary_tree(root):
    if root is None:
        return None
    
    left = mirror_binary_tree(root.left)
    right = mirror_binary_tree(root.right)
    root.left = right
    root.right = left
    
    return root