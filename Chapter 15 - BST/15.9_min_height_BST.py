# create min height BST from sorted array

def array_to_BST(A, start = 0, end = len(A)):
	if start >= end:
		return None
	mid = start + (end - start) / 2

	tree = BST(A[mid])
	tree.left = array_to_BST(A, start, min-1)
	tree.right = array_to_BST(A, mid+1, end)
	return tree