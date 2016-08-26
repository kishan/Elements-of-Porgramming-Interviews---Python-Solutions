"""
You are given pre-order traversal with a slight modification. 
It includes null pointers when a particular node has nil left/right child. 
Reconstruct the binary tree with this information.

Ex. [H, B, F, None, None, E, A, None, None, None, C, None, D, None, G, I, None, None, None]

     H
   /   \
  B     C
 / \     \
F   E     D
   /       \
  A         G
           /
          I
"""

# time: O(n)
def contruct_tree(pre_order, index=0):
    index += 1
    if index >= len(pre_order):
        raise IndexError('wtf is wrong with you?')

    root = pre_order[index]
    if root is None:
        return (None, index)


    node = BST(root)
    node.left, index = construct(pre_order, index)
    node.right, index = construct(pre_order, index)

    return (node, index)


# my solution without recursion
# works?

def contruct_tree(pre_order):
    tree = BST(pre_order[0])
    curr = tree
    stack = []
    i = 0
    while i < len(pre_order)-1:
        if curr is not None:
            curr.left = L[i+1]
            stack.append(curr)
            cur = curr.left
        else:
            curr = stack.pop()
            curr.right = L[i+1]
            cur = curr.right

    return tree

