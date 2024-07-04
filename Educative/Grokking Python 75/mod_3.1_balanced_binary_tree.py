# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/4890762642849792

from utils import TreeNode

'''
NOTES:
    In official solution, the helper function, which only returns the
    height of a node, uses and returs -1 to indicate that an imbalance
    has been detected somewhere in the tree
'''

def is_balanced(root):
    res, _ = is_balanced_helper(root)
    return res

def is_balanced_helper(node):
    if node is None:
        return True, 0

    left_bal, left_height = is_balanced_helper(node.left)
    right_bal, right_height = is_balanced_helper(node.right)
    curr_height = 1 + max(left_height, right_height)

    if left_bal and right_bal:
        return abs(left_height - right_height) < 2, curr_height
    return False, curr_height