# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/5885749262155776

from utils.BinaryTree import TreeNode
from collections import deque

def find_max_depth(root):
    if root is None:
        return 0
    left = find_max_depth(root.left)
    right = find_max_depth(root.right)
    return 1 + max(left, right)