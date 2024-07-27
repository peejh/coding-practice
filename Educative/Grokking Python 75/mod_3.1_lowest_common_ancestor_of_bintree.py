# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/6029705258074112

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from utils import TreeNode

class Solution:
    def lowest_common_ancestor(self, current_node, p, q):

        def helper(root):
            if root is None:
                return False
            
            curr_found = root == p or root == q
            left_found = helper(root.left)
            right_found = helper(root.right)

            if isinstance(left_found, TreeNode):
                return left_found
            
            if isinstance(right_found, TreeNode):
                return right_found
            
            if curr_found + left_found + right_found > 1:
                return root

            return curr_found or left_found or right_found

        return helper(current_node)