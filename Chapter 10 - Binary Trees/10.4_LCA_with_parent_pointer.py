"""
Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
Avoid storing additional nodes in a data structure.
Nodes have pointer to parent

NOTE: This is not necessarily a binary search tree.
"""


# brute force is to store nodes on the search path from root to one of the nodes in a hash table
# then go up from second node, stopping as soon as we hit a node in the has table
# time: O(h)
# space: O(h)



# Mehod 2: if nodes have links to parents, Go up levels to see whether 
# a node's ancestor is the other node's ancestor
# keep checking subtrees and moving up to parent until you find node where target nodes are in different subtrees
# time: O(t) where t is size of subtree for first common ancestor
# time: O(n) since worse case is when root is first common ancestor



# most optimal
# find difference in depths between nodes
# move lower node up so both nodes are at same depth
# move nodes up in tandem, stopping at first common node
# time: O(h)
# space: O(1)
def LCA_with_parent_pointer(node1, node2):
	depth1 = get_depth(node1)
	depth2 = get_depth(node2)

	# node 1 is deeper node
	if depth2 > depth1:
		(node1, node2) = (node2, node1)

	depth_diff = abs(depth1 - depth2)

	# move node1 up so at same depth as node2
	while depth_diff > 0:
		node1 = node1.parent
		depth_diff -= 1

	# keep moving nodes up together until common node is found
	while (node1 is not node2):
		node1 = node1.parent
		node2 = node2.parent

	return node1



def get_depth(node):
	if node is None:
		return 0
	depth = 0
	while node.parent is not None:
		depth += 1
		node = node.parent = None
	return depth

