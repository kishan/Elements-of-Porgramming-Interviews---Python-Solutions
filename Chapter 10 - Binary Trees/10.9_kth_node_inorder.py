"""
compute the kth node apearing in an inorder (left, node, right) traversal 
(same as finding kth smallest node in BST)
"""

def SizeOfTree(root):
    if root is None:
        return 0
    size = SizeOfTree(root.left) + SizeOfTree(root.right) + 1
    return size
        
def kth_node(root, k):
    if root is None:
        return None
        
    leftsize = SizeOfTree(root.left)
    if leftsize == k-1:
        return root
    elif leftsize > k-1:
        return kthSmallest(root.left,k)
    else:
        return kthSmallest(root.right,(k-1-leftsize))           


# more efficient solution? (without checking size?)