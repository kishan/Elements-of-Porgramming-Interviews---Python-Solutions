# write a program that takes an input as a binary tree and performas 
# 	an inorder traversal of the tree. Do not use recursion
# (node -> left subtree -> right subtree)


# solution: use stack
# go to left subtree and add node to stack
# if node is None: then take of node off stack, add to solution, then go to right subtree

# time: O(n)
# space: O(h)
def preorderTraversal(self, root):
    solution = []
    stack = []
    curr = root
    while curr != None or len(stack)>0:
        if curr != None:
            solution.append(curr.data)
            stack.append(curr.right)
            curr = curr.left
        else:
            curr = stack.pop()
    return solution