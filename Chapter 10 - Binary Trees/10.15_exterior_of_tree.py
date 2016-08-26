"""
return list of exterior nodes of binary tree in counter-clockwise direction
(includes nodes on left edge, at bottom (leafs), nodes on right edge)


     H
   /   \
  B     C
 / \     \
F   E     D
   /     / \
  A     K   G
           /
          I
         /
        J


=> [H, B, F, A, K, J, I, G, D, C]
"""

def exterior(root):
	if root is None:
		return []

	L = []

	L.append(root)

	left_exterior(root.left, True)

	right_exterior(root.right, True)

def is_leaf(node):
	if node is None:
		return False

	return (node.left is None) and (node.right is None)


def left_exterior(node, True):
	if node is not None:
		if is_leaf(node) or is_boundary:
			L.append(node)


	left_exterior(root.left, is_boundary)

	# right subtree is still on boundary if cur node is on boundary there is not left subtree
	right_is_boundary = is_boundary and (node.left is None)
	left_exterior(root.right, right_is_boundary)


def right_exterior(node, True):
	# left recursive call needs to be first to make sure exterior is in counter-clockwise direction
	left_is_boundary = is_boundary and (node.right is None)
	right_exterior(root.left, left_is_boundary)

	# right recursive call
	# must be before lead and boundary check to make sure nodes on right boundary are added from bottom up
	right_exterior(root.right, is_boundary)

	if node is not None:
		if is_leaf(node) or is_boundary:
			L.append(node)


	

	
	

def right_exterior(node, list, is_boundary)
    return nil if node.nil?

    # Insert node if its a boundary node as indicated by parent
    # or if its a leaf node
    if is_leaf? || is_boundary
        list << node
        return
    end

    # Traverse to the next node
    if node.left.exists?
        is_boundary = is_boundary && node.right.nil?
        right_exterior(node.left, list, is_boundary)
    elsif node.right.exists?
        right_exterior(node.right, list, is_boundary)
    end
end