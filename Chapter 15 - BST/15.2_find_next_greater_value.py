# write a function that takes a node and a value, and returns first key that 
# 	would appear in an inorder traversal which is greater than the input value


# if value is less than or equal to k, search right subtree
# if value is greater than k, update first_so_far and search in left subtree



# recrusive
# O(h) time and O(h) space
def next_value(node, k, first_so_far = None):
	if node is None:
		return first_so_far
	if node.data > k:
		return next_value(node.left, k, node.data)
	else:
		return next_value(node.right, k, first_so_far)



# non-recursive
# O(h) time and O(1) space
def next_value(node, k):
	while (node is not None):
		if node.data > k:
			next_val = node.data
			node = node.left
		else:
			node = node.right
	return next_val

