#Implement a function to check if a binary tree is balanced. For the purposes of
#this question, a balanced tree is defined to be a tree such that the heights of the
#two subtrees of any node never differ by more than one.


#O(n^2) naive algorithm
# This is called 2*n times
def is_balanced_binary_tree(btree):
    #compare depths of both sides
    if btree is None: return True
    return (abs(height(btree.left) - height(btree.right)) <= 1) and
        is_balanced_binary_tree(btree.left) and is_balanced_binary_tree(btree.right)

# Time complexity: O(nlog(n)) ?
# each node is touched once by each node above it
def height(btree):
    if btree is None:
        return 0
    else: 
        return 1 + max(height(btree.left), height(btree.right))

##########################################################################################
##########################################################################################
##########################################################################################

#effcient algorithm, get heights of subtrees and check subtrees if balanced at the same time
# time: O(n)
# space: O(h)
def is_balanced_binary_tree2(btree):
    if btree is None: return True
    return check_balanced(btree)[0]
    
def check_balanced(btree):
    if btree is None:
        return (True, 0)
    left_balanced, left_depth = check_balanced(btree.left)
    right_balanced, right_depth = check_balanced(btree.right)
    btree_depth = 1 + max(left_depth, right_depth)
    is_balanced = left_balanced and right_balanced and
        (abs(left_depth - right_depth) <= 1)
    return (is_balanced, btree_depth)



