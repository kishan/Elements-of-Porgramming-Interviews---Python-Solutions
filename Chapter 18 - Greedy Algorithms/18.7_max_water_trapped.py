"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
Compute the maximum water trapped by a pair of vertical lines An array of integers naturally defines a set of lines parallel to the Y-axis, starting from x = 0

An array of integers naturally defines a set of lines parallel to the Y-axis, starting from x = 0. 
The goal of this problem is to find the pair of lines that together with the X-axis "trap" the most water.
Write a program which takes as input an integer array and returns the pair of entries 
	that trap the maximum amount of water. 

Ex. {1, 2, 1, 3, 4, 4, 5, 6, 2, 1, 3, 1, 3, 2, 1, 2, 4, 1} 
		=> 48 (bcz area between indices 4 and 16 is the max water that can be trapped)

"""
# solution:
# start with one pointer at each end of the array
# continue moving pointers torwards the center
# move which ever pointer has smaller height

# A is list of heights
def max_area(A):
	i = 0
	j = len(A) - 1
	max_area = -1

	while (i<j):
		width = j-i
		height = min(A[i],A[j])
		cur_area = width*height

		max_area = max(max_area, cur_area)

		if cur_area > max_area:
			max_area = cur_area
		if A[i] < A[j]:
			i += 1
		elif A[i] > A[j]:
			j -= 1
		else:
			i += 1
			j -= 1
	return max_area