# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/5535637352611840

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

def diameter_of_binaryTree(root):
  root_height, root_diameter = get_heights_diameter(root)
  return root_diameter 
  # return get_heights(root, 0)[1]

def get_heights_diameter(node):
  if not node:
    return (0, 0)
  left_height, left_diameter = get_heights_diameter(node.left)
  right_height, right_diameter = get_heights_diameter(node.right)
  curr_diameter = max(left_height + right_height, left_diameter, right_diameter)
  curr_height = max(left_height, right_height)
  return (1 + curr_height, curr_diameter)