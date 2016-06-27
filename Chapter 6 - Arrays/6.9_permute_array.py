# Ex. [2,0,1,3] and [a,b,c,d] => [b,c,a,d]
# maps element at index 0 to index 2
# maps element at index 1 to index 0


def permute_elements(A,B):
	n = len(A)
	for i in xrange(n):
		old = A[i] % n
		target_old = A[old] % n
		target_new = i
		A[old] = target_new*n + target_old
	
	for i in xrange(n):
		A[i] = B[A[i]/n] 

	return A

A = [2,0,1,3]
B = ["a", "b", "c", "d"]
print permute_elements(A,B)
# ['b', 'c', 'a', 'd']