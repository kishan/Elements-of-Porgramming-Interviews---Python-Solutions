# write insert and delete function for BST



# go down tree until you find end of tree where key should be inserted
def insert(root, key):
	if root is None:
		return BST(key)

	curr = root
	# find where new key should be inserted
	while (cur is not None):
		parent = cur
		if key == curr.data:
			return False
		elif (key < curr.data):
			cur = cur.left
		else:
			cur = cur.right

	# insert new key
	if key < parent.data:
		parent.left = BST(key)
	else:
		parent.right = BST(key)


# if node with key has right subtree, replace node with next successor (left most child of right subtree)
# else: doesn't have right subtree so replace node with key with left subtree
def delete(root, key):
	# find node with key
	curr = root
	parent = None
	while (curr is not None) && (curr.data != key):
		parent = curr
		if key < curr.data:
			curr = curr.left
		else:
			curr = curr.right

	# no node with key found
	if curr is None:
		return False

	keyNode = curr
	if keyNode.right is not None:
		# find min of right subtree
		rKeyNode = keyNode.right
		rParent = keyNode

		while (rKeyNode.left is not None):
			rParent = rKeyNode
			rKeyNode = rKeyNode.left

		# replace node with key, with successor's data
		keyNode.data = rKeyNode.data

		# delete successor
		if rParent.left == rKeyNode:
			rParent.left = rKeyNode.right
		else:
			rParent.right = rKeyNode.right

		# delete rKeyNode's connection to the graph
		rKeyNode.right = None

	# if node with key doesn't have right subtree
	else:
		# update root link if needed
		if root == keyNode.left:
			root = keyNode.left
			keyNode.left = None
		else:
			if parent.left = keyNode:
				parent.left = keyNode.left
			else:
				parent.right = keyNode.right
			keyNode.left = None

	return True










