# write function thtat takes BST and integer k, and returns k largest
# 	elements in the BST in decreasing order


def largest_k(node, k, L=[]):
	if (node is not None) and (len(L)<k):
		largest_k(node.right, k, L)
		if len(L) < k:
			L.append(node.data)
			largest_k(node.left, k, L)


# my solution
# works?
def largest_k(node, k):
	n = get_size(node.right)
	if n >= k:
		return largest_k(node.right, k)
	else:
		return largest_k(node.left, k-n-1) + [node.data] + largest_k(node.right, n)


