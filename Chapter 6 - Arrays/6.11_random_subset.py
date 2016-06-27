import random

# improve space by drawing random element to swap with current i = [1:k]
# runtime O(k)
# space O(1)
def random_subset(A, k):
	for i in range(k):
		idx = random.randint(i, len(A)-1)
		A[i], A[idx] = A[idx], A[i]
	return A[:k]


A = [1,2,3,4,5,6,7,8,9]
print random_subset(A, 4)

