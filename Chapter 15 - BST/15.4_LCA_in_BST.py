# form BST from pre-order sequence (root => left subtree => right subtree)

# solution
# first element in list is root
# all elements to right of root that are less than root, are in left subtree
# all elements to right of root that are greater than root, are in right subtree


def build_BST(L):
	return build_BST_helper(L, 0, len(L))


# worst case: T(n) = O(n) + T(n-1)   =>  O(n^2)
# balanced BST: T(n) = O(n) + T(n/2)   =>  O(nlog(n))
def build_BST_helper(L, start, end):
	if start >= end:
		return None

	transition_point = start + 1
	while (transition_point < end) and (L[transition_point] < L[start]):
		transition_point += 1

	root = L[start]
	final = BST(root)
	final.left = build_BST_helper(L, start + 1, transition_point)
	final.right = build_BST_helper(L, transition_point, end)
	return final


# above solution does repreasted passes over nodes
# there is more optimal O(n) solution

