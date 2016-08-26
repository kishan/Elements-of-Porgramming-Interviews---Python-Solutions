# recreate binary tree from inorder and preorder traversal sequences
# assume each node has a unique key

# solution:
# user first element in preorder list to find what the root is
# using this root, find what index it is in the inorder list
# all elements before this index in the inorder list are in the left subtree
# all elements after this index in the inorder list are in the right subtree
# from two above facts you will also know how many elements each subtree has
# 	allowing you to properly split up preorder list too into left subtree and right subtree



# I = inOrder list
# P = preOrder list
def build_BST(I, P):
	if (len(I) == 0) and (len(P) == 0):
		return None

	root_val = P[0]
	root_index_I: I.index(root_val)

	P = P[1:]
	tree = BST(root_val)

	I_left = I[:root_index_I]
	I_right = I[root_index_I+1:]
	P_left = P[:root_index_I]
	P_right = P[root_index_I:]

	tree.left = build_BST(I_left, P_left)
	tree.right = build_BST(I_right, P_right)

	return tree

# solution above is O(nlog(n)) time
# space can be saved by using list indices instead of making recursive with new list
# time can be reduced by O(n) by using hash table to map nodes to index for inOrder 
# 	list to prevent having to search through list to find index of a node












