# delete duplicates from sorted array
# return number of valid elements
# dups can be moved to end of array (values can be anything)
# [1,2,3,3,4,5,6,6,6,7,8] => [1,2,3,4,5,6,7,8,0,0,0]

# solution with O(n) space
# use hash table to find out which elements are duplicates
# copy new elements back in array

# solution with O(1) space but O(n^2) time
# iterate through L, if L[i] == L[i+1], shift all 
# 	elements at and after i+2 to the left by one

# O(1) space and O(n) solution
def remove_dups(L):
	write_index = 1
	for i in xrange(1, len(L)):
		if L[i] != L[i-1]:
			write_index += 1
			swap(L, i, write_index)
	return write_index



def swap(L, i1, i2):
	(L[i1], L[i2]) = (L[i2], L[i1])