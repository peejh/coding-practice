# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/5188600086003712

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

from utils import TreeNode
from math import inf


def validate_bst_v1(root):
    # This was written without reading the suggested way of solving
    # the problem.

    def helper(node):

        if node is None:
            return (True, [])
        
        left_valid, left_tree = helper(node.left)
        right_valid, right_tree = helper(node.right)

        curr_valid = left_valid and right_valid

        if curr_valid and left_tree != []:
            curr_valid = left_tree[-1] < node.data

        if curr_valid and right_tree != []:
            curr_valid = right_tree[0] > node.data

        elems = left_tree + [node.data] + right_tree

        return (curr_valid, elems)

    return helper(root)[0]


def validate_bst_v2(root):
    # This solution uses inorder traversal and a single variable to
    # track the previous number in the binary tree.
    # If the whole tree is traversed and the number in the current
    # node is always higher than the tracked previous number, then
    # the tree is a valid BST.
    # The official solution is a variant of this version.

    prev = -inf

    def inorder(node):

        nonlocal prev # `nonlocal` works like `global` keyword but works
                      # for nested functions

        if node is None:
            return True

        left_valid = inorder(node.left)

        if not left_valid:
            return False

        if prev >= node.data:
            return False
        
        prev = node.data

        return inorder(node.right)

    return inorder(root)


def validate_bst_v3(root):
    # A way cleaner implementation.
    # Uses inorder traversal to convert the tree into a list, and
    # checks if the resulting list is in ascending order.

    def inorder(node):
        if node is None:
            return []

        left = inorder(node.left)
        right = inorder(node.right)

        return left + [node.data] + right

    bst = inorder(root)

    for i in range(1, len(bst)):
        if bst[i] <= bst[i-1]:
            return False

    return True