# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/6692112628318208

from utils import TreeNode

# VERSION 1     
def right_side_view(root):

    return right_side_view_helper(root, [], 0)

def right_side_view_helper(root, rights, level):
    '''
    NOTES:
    - this solution works because the whole recursion references
      the same answer list, i.e. `rights`
    - rightmost elements are added to the answer list on a FCFS
      basis
    '''

    # base case
    if root is None:
        # empty list return value is only relevant if the actual 
        # root node is null, otherwise, the return statement is
        # mainly to prevent errors and to stop the recursion
        return [] 

    # add the rightmost data to the answer list
    if len(rights) == level:
        rights.append(root.data)

    # visit child nodes starting with right node first
    right_side_view_helper(root.right, rights, level + 1)
    right_side_view_helper(root.left, rights, level + 1)

    return rights


# VERSION 2
def right_side_view2(root):
    res = []
    right_side_view_helper2(root, res, 0)
    return res

def right_side_view_helper2(root, rights, level):

    if root is None:
        return

    if len(rights) == level:
        rights.append(root.data)

    right_side_view_helper(root.right, rights, level + 1)
    right_side_view_helper(root.left, rights, level + 1)