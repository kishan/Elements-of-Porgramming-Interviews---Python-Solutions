# given two nodes and a middle node, check if one node is an
# 	ancestor to the middle node and the other node is a descendant 
# 	of the middle node. Middle node not allowed to be equal to either nodes. 


# solution
# O(h) time
# check if first node is ancestor of middle node
# if so: check if middle node is ancestor to second node

# if first node is not ancrstor of middle node, 
# 	check if second node is ancestor of middle node and
# 	then check if middle node is ancestor to first node


# improvement
# O(d) where d is difference between depth of ancestor and descendant

# we can prevent searching whole height of tree by performing searches
# 	for middle node from both nodes at same time in interweaved fashion
# once one node comes across middle node, then run search for other node from middle node
