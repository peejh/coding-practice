# https://www.educative.io/module/page/k5m3gACXwNz5Z6J0E/10370001/6660878585954304/5568026019758080

from utils import TreeNode

def serialize(root):
    if root is None:
        return [None]

    res = [root.data]
    res.extend(serialize(root.left))
    res.extend(serialize(root.right))

    # print(res)
    return res

def deserialize(stream):
    # print(stream)
    root, _ = deserialize_recursive(stream)
    return root

def deserialize_recursive(stream):
    # print(stream)
    if stream[0] is None:
        return None, stream[1:]
    node = TreeNode(stream[0])
    node.left, stream = deserialize_recursive(stream[1:])