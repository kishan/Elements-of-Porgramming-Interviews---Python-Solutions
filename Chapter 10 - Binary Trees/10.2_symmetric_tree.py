"""
Given a binary tree, check whether it is a mirror of itself.

For example, this binary tree is symmetric:

     1
   /   \
  2     2
 / \   / \
3   4 4   3
But the following is not:

    1
   / \
  2   2
   \   \
   3    3

"""


def check_symmetric(A, B):
	if A is None and B is None:
		return True
	elif ((A is not None) and (B is not None)):
		return (A.data == B.data) 
			and check_symmetric(A.left, B.right) 
			and check_symmetric(A.right, B.left)
	# one subtree is empty, and the other is not
	return False