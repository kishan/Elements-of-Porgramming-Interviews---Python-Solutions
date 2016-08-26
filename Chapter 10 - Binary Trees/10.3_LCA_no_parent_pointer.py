"""
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
Avoid storing additional nodes in a data structure.
Nodes do not have pointer to parent

NOTE: This is not necessarily a binary search tree.
"""


# start at root
# keep traversing down subtree that contains both p and q
# if p and q are in different subtrees, then return 
#		current node which represents first common acenstor
# Time complextity: O(n^2)

def first_common_ancestor(bst, p, q):
	# make sure p and q are in the tree
    if not in_subtree(bst.root, p) or not in_subtree(bst.root, q):
        return None
    return first_common_ancestor1(bst.root, p, q)

def first_common_ancestor1(x, p, q): # pass root in
    if x is None:
        return None
    if x == p or x == q:
        return x
    is_p_on_the_left = in_subtree(x.left, p)
    is_q_on_the_left = in_subtree(x.left, q)
    # p and q are in different branches so x must be first common ancestor
    if is_p_on_the_left != is_q_on_the_left:
        return x
    # both p and q in left branch
    if is_p_on_the_left:
        return first_common_ancestor1(x.left, p, q)
    # both p and q in right branch
    else:
        return first_common_ancestor1(x.right, p, q)



# more optimal solution
# return how many nodes of two target nodes were present in subtree
# avoid having to perform multiple passes
# Time complextity: O(n)
def LCA(tree, node1, node2):
    if tree is None:
        return [0, None]

    [left_num, LCA_left] = LCA(tree.left, node1, node2)
    if LCA_left is not None:
        # found LCA in left subtree
        return [-1, LCA_left]

    [right_num, LCA_right] = LCA(tree.right, node1, node2)
    if LCA_right is not None:
        # found LCA in right subtree
        return [-1, LCA_right]


    num_target_nodes = left_num + right_num 
                                + (1 if tree == node1 else 0) 
                                + (1 if tree == node2 else 0) 
                                
    if num_target_nodes == 2:
        # current node is LCA
        return [-1, tree]
    else:
        return [num_target_nodes, None]