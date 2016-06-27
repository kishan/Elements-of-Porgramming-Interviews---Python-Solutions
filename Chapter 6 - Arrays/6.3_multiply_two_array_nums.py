# first thought: create separate array for each multuplication row
# 				 add all arrays up after
# -> takes up a lot of space

# possible to add together columns on the go? => Yes!


def multiply(A, B):
	sign = 1
	if A[0] < 0:
		sign *= -1
		A[0] = abs(A[0])
	if B[0] < 0:
		sign *= -1
		B[0] = abs(B[0])


	final_len = len(A)+len(B)
	final = [0]*(final_len)
	for i in xrange(len(A)-1, -1, -1):
		for j in xrange(len(B)-1, -1, -1):
			index = i + j + 1
			final[index] = final[index] + (A[i]*B[j])
	print final
	# deal with carries
	carry = 0
	for i in xrange(final_len-1, -1, -1):
		cur = final[i] + carry
		final[i] = cur%10
		carry = cur/10	


	# remove leading zeroes
	i = 0
	while final[i] == 0:
		i += 1
	final = final[i::]

	# edge case
	if len(final) == 0:
		return [0]

	# add negative value if necessary
	final[0] *= sign

	return final



# Example:
# C = [1,2,3]
# D = [4,5,6]

# + 		 [6, 12, 18]
# + 	 [5, 10, 15]
# +   [4, 8, 12]
# ____________________________
# [0, 4, 13, 28, 27, 18] => [5, 6, 0, 8, 8]





# C = [1,2,3]
# D = [4,5,6]
# print multiply(C,D)






