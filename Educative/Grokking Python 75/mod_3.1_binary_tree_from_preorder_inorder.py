# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/5982079338807296

from utils import TreeNode

def build_tree(p_order, i_order):

    # When `p_order` list is empty, there is no more
    # data to insert, hence, return None
    if not p_order:
        return None
    
    # Create a TreeNode from the first element of
    # the `p_order` list
    data = p_order[0]
    root = TreeNode(data)
    root_i = i_order.index(data)
    left_len = root_i # renaming for readability

    # Build the left and right child nodes of `root`
    # Pass sliced copies of `p_order` and `i_order` based
    # on the number of elements in the left subtree, and the
    # index of the root element in `i_order`, respectively
    root.left = build_tree(p_order[1:left_len+1], i_order[:root_i])
    root.right = build_tree(p_order[left_len+1:], i_order[root_i+1:])

    return root