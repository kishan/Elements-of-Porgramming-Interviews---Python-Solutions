# check is BST is valid



# turn BST into array using in-order traversal
# check if array is sorted
# *** This method can't handle duplicate values
# Space complexity: O(n)
# Time complexity:  O(n)
def in_order_search(btree):
	if btree is None: return []
	return in_order_search(btree.left) + [btree.content] + in_order_search(btree.right)

def valid_bsearch_tree(btree):
	#in-order method
	l = in_order_search(btree)
	if sorted(l) == l:
		return True
	return False


# Assuming no repeated elements
# traverse in order without array
# Space complexity: O(log(n))
# Time complexity:  O(n)
def is_bst_in_order(x, low_bound = None):
    if x is not None:
        if not is_bst_in_order(x.left, low_bound):
            return False
        if low_bound is not None and not(low_bound < x.key):
            return False
        low_bound = x.key
        if not is_bst_in_order(x.right, low_bound):
            return False
    return True


# recursive method
# use (min, max) bound and pass down to children
# Space complexity: O(log(n))
# Time complexity:  O(n)
def valid_bsearch_tree(btree, min = None, max = None):
	if btree is None: return True
	return (min is None or btree.content > min) and 
			(max is None or btree.content <= max) and
			valid_bsearch_tree(btree.left, min, btree.content) and
			valid_bsearch_tree(btree.right, btree.content, max)


