"""
Given an array and a value, find if there is a triplet in array whose sum is equal to the given value. 
If there is such a triplet present in array, then print the triplet and return true. 
Else return false. 

Ex. [12, 3, 4, 1, 6, 9] and given sum is 24 => (12, 3 and 9) present in array whose sum is 24.
"""

def two_sum(L, target):
	L.sort()
	i = 0
	j = len(L) - 1
	while i < j:
		sum_ = L[i] + L[j]
		if sum_ == target:
			return (L[i], L[j])
		elif sum_ < target:
			i += 1
		else:
			j -= 1
	return None


def three_sum(L, target):
	L.sort()
	for x in L:
		if two_sum(L, target - x):
			return True
	return False