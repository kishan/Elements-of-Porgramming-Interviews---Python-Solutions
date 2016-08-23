# given a range and a BST, return value of keys that fall within the given range
"""
Algorithm:

1) If value of root’s key is greater than k1, then recursively call in left subtree.
2) If value of root’s key is in range, then print the root’s key.
3) If value of root’s key is smaller than k2, then recursively call in right subtree.
"""
def nodes_in_range(root, low, high, result = []):
	if root is None:
		return

	if low < root.data:
		nodes_in_range(root.left, low, high, result)

	if (low <= root.data <= high):
		result.append(root.data)

	if root.data < high:
		nodes_in_range(root.right, low, high, result)

