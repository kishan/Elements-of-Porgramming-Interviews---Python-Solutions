# write a program that takes an input as a binary tree and performas 
# 	an inorder traversal of the tree. Do not use recursion
# (left subtree -> node -> right subtree)


# solution: use stack
# go to left subtree and add node to stack
# if node is None: then take of node off stack, add to solution, then go to right subtree

# time: O(n)
# space: O(h)
def inorderTraversal(root):
    stack = []
    node = root
    solution = []
    while node != None or len(stack)>0:
        if node != None:
            stack.append(node)
            # go left
            node = node.left
        else:
        	# going up
            node = stack.pop()
            solution.append(node.val)
            # going right
            node = node.right
    return solution