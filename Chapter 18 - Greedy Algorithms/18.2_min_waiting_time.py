# find shortest wait time

# Ex. [2,5,1,3] 
# 		if ordered as [2,5,1,3], then wait = 0 + (2) + (2+5) + (2+5+1) = 17
# 		if ordered as [5,3,2,1], then wait = 0 + (5) + (5+3) + (5+3+2) = 23
# 		if ordered as [1,2,3,5], then wait = 0 + (1) + (1+2) + (1+2+3) = 10
# min_wait = 10


# solution:
# times should be ordered in increasing order


def min_wait(L):
	L.sort()
	total_wait_time = 0
	for i in xrange(len(L)):
		num_remaining = (len(L) - i - 1)
		total_wait_time += L[i] * num_remaining

	return total_wait_time