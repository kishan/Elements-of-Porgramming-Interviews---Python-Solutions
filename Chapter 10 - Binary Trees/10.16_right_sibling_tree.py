"""
write a program that takes a PERFECT BINARY TREE and sets each node's level-next 
	field to the node on its right (at the same depth) if it exists

Note: tree given is a perfect binary tree
"""

# assuming all nodes have node.next set as None as default
# time: O(n)
# space: O(1)
def construct_right_sibling(root):
	left_start = root
	while (left_start is not None) and (left_start.left is not None):
		populate_lower_level_next_field(left_start)
		# go down to next level starting node
		left_start = left_start.left


def populate_lower_level_next_field(start_node):
	node = start_node
	while (node is not None):
		# populate left chid's field
		node.left.next = node.right

		# populate right child's field
		# right child should point to node's next left child
		if (node.next is not None):
			node.right.next = node.next.left

		# go to next node on same level
		node = node.next


##############################################################################
##############################################################################
##############################################################################



# recursive solution
# this also makes nodes on right edge point to None
# time: O(n)
# space: O(h)
def construct_recursive(node):
	if node is None:
		return

	if (node.left is not None):
		node.left.next = node.right


	# populate right child's field
	# right child should point to node's next left child
	if (node.right is not None):
		if node.next is not None:
			node.right.next = node.next.left
		else:
			node.right.next = None

	construct_recursive(node.left)
	construct_recursive(node.right)
