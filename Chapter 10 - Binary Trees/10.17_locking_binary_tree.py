"""
A binary tree node can be locked or unlocked only if none of its parents or children are locked. 
Assume each node has parent pointer. 

Write the following methods:
    * to test if a node is locked
    * to lock a given node (should return True if we were able to lock else False)
    * to unloack a given node,

# brute force- keep is_locked bool field for each node => requries O(n) to lock (would have all subtrees)

SOLUTION
For each node keep track of the number of nodes in its subtree that are locked
To lock,
    -check child locked count
    -check all nodes in the path to parent
    -if none of the above are locked, then mark node as locked
To unlock
    -mark node as unlocked
    -update all nodes in the path to parent and decrement their lock count

"""

class BinaryTreeNode:
    left = None
    right = None
    parent = None
    lock_count = 0
    is_locked = False

    def lock():
        return False if self.lock_count != 0

        # Check all nodes on path to parents if they are locked
        iter = self.parent
        while iter:
            if iter.is_locked:
                return False
            iter = iter.parent

        self.is_locked = True

        # Update lock count for all nodes on path to parent
        iter = self.parent
        while iter:
            iter.lock_count += 1
            iter = iter.parent

        return True

    def unlock
        if self.is_locked == False:
            return False

        self.is_locked = False

        # Update all nodes on path to parent
        iter = self.parent
        while iter
            iter.lock_count -= 1
            iter = iter.parent

        return True
 