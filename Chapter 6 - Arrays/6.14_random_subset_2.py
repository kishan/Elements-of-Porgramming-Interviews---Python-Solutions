__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

"""
Same as 6.11 (create random subset) but don't modify original array
"""
import random

# idea: based on Ex. 11 but do not swap in original array
#  	  => simulate swapping using hashtable
# runtime: O(k); space: O(k)
def randomSubset(n, k):
	swapped = {}
	final = [None]*k
	for i in xrange(k):
		j = random.randint(i, n-1)
		if j in swapped:
			val = swapped[j]
		else:
			val = j
		final[i] = val
		if i in swapped:
			swapped[j] = swapped[i]
		else:
			swapped[j] = i
	return final


# Ex. n=100, k = 4
# [None, None, None, None]
# j = 28 
# 	[28, None, None, None]
#   swapped = {28:0}
# j = 42
# 	[28, 42, None, None]
#   swapped = {28:0, 42:1}
# j = 28
# 	[28, 42, 0, None]
#   swapped = {28:2, 42:1, 2:0}
# j = 64
# 	[28, 42, 0, 64]
#   swapped = {28:2, 42:1, 2:0, 64:3}
# return [28, 42, 0, 64]]