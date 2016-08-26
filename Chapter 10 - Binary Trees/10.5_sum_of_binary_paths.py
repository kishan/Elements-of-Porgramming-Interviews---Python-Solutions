"""
Consider a binary tree in which each node contains a binary digit

Design an alogirthm to compute the sum of the binary numbers represented by the root-to-leaf paths
"""

def sum_to_root(node, partial_sum=0):
	if node is None:
		return 0

	partial_sum = partial_sum*2 + node.data

	if (node.left is None) and (node.right is None):
		return partial_sum
	else:
		return sum_to_root(node.left, partial_sum) + sum_to_root(node.right, partial_sum)
