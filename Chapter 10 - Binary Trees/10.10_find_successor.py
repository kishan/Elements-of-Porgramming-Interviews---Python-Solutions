"""
successor is next node in inorder traversal
Assume each node has a link to its parent
(same as finding next node of a given node in a BST)
"""

# Write an algorithm to find the 'next'node (i.e., in-order successor) of a given node in
# a binary search tree. You may assume that each node has a link to its parent.


# if x has right node, then next node is left most child of x.right
# if x.right is None, then must traverse up tree
# need to look for parent greater than current node
def find_next(x):
    if x is None:
        return None
    if x.right is not None:
        return left_most_child(x.right)

    # keep traversing upward until node is left tree of parent
    while (x.parent is not None) and (x.parent.right == x):
        x = x.parent

    # parent is either None or next node
    return x.parent


def left_most_child(x):
	if x is None:
		return None

    while x.left in not None:
        x = x.left
    return x