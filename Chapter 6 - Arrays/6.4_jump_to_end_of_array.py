# return whether it is possible to reach last index starting from beginning of array
def canReachEnd(L):
	max_jump_index = 0
	for i in xrange(len(L)):
		if max_jump_index < i:
			return False
		max_jump_index = max(max_jump_index, i + L[i])
	return True