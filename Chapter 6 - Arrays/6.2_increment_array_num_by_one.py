#  my own implementation

def add_one_to_array(A):
	if len(A) == 0: return [1]
	carry = 1
	for i in xrange(len(A)-1, -1, -1):
		cur = carry + A[i]
		A[i] = cur%10
		carry = cur/10
	if carry == 1:
		return [1] + A
	# remove leading zeroes
	else:
		i = 0
		while A[i] == 0:
			i += 1
		# start from first non-zero
		return A[i::]
