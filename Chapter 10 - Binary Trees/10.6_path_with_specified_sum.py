"""
Consider a binary tree in which each node is labeled with an integer

The path weight of a node is the sum of the integers on the unique path from the root to that node

Write a program which takes an integer and a binery tree with integer node weights, and 
	checks if there exists a lead whose path weigth equals the given integer

"""

def exists_path_sum(node, target_sum, partial_sum=0):
	if node is None:
		return False

	partial_sum += node.data

	if (node.left is None) and (node.right is None):
		# is leaf
		return partial_sum == target_sum
	else:
		return exists_path_sum(node.left, target_sum, partial_sum) 
			or exists_path_sum(node.right, target_sum, partial_sum)
