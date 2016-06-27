import random
"""
given number n, return numbers from 0 to n-1 randomly shuffled
"""
# improve space by drawing random element to swap with current i = [1:k]
# runtime O(k)
# space O(1)
def random_shuffle(n):
	A = range(n)
	for i in xrange(n):
		idx = random.randint(i, len(A)-1)
		A[i], A[idx] = A[idx], A[i]
	return A


print random_shuffle(4)

