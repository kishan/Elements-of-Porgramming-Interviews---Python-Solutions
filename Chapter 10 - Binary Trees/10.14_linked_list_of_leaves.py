"""
given a binary tree, compute a linked list from the leaves of the binary tree.
The leaves should appear in left-to-right order

How would you do it for doubly linked list?

Ex.
     H
   /   \
  B     C
 / \     \
F   E     D
   /       \
  A         G
           /
          I

=> [F,A,I]

"""

curr = LinkedList()
def linked_leaves(node):
	if node is not None:
		if (node.left is None) and (node.right is None):
			curr.next = LinkedList(node.data)

			# only if making double linkedlist
			curr.next.prev = curr

			curr = curr.next

		linked_leaves(node.left)
		linked_leaves(node.right)