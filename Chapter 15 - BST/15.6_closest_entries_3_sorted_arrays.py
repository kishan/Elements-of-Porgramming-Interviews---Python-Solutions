# design an algorithms that takes three sorted arrys and returns one entry 
# 	from each such that the minimum intreval containing these three entires 
#	is as small as possible. 

# Ex. [5, 10, 15] & [3,6,9,12,15] & [8, 16, 24]   => [15, 15, 16]

"""
A Simple Solution is to run three nested loops to consider all triplets from A, B and C. Compute the value of max(abs(A[i] – B[j]), abs(B[j] – C[k]), abs(C[k] – A[i])) for every triplet and return minimum of all values. Time complexity of this solution is O(n3)


A Better Solution is to us Binary Search.
1) Iterate over all elements of A[],
      a) Binary search for element just smaller than or equal to in B[] and C[], and note the difference.
2) Repeat step 1 for B[] and C[].
3) Return overall minimum.

Time complexity of this solution is O(nLogn)
"""


# solution
# take min number from each list
# then remove lowest number in tuple, and replace it with next greatest 
#	number from the same array the lowest number in tuple was originally from.
# continue process, and then return tuple combination that had min interval
"""
1)   Start with i=0, j=0 and k=0 (Three index variables for A,
                                  B and C respectively)

//  p, q and r are sizes of A[], B[] and C[] respectively.
2)   Do following while i < p and j < q and k < r
    a) Find min and maximum of A[i], B[j] and C[k]
    b) Compute diff = max(X, Y, Z) - min(A[i], B[j], C[k]).
    c) If new result is less than current result, change 
       it to the new result.
    d) Increment the pointer of the array which contains 
       the minimum.
"""

def min_gap(A, B, C):
	diff = 1000
	min = 1000
	min = -1
	while (i<len(A)  and j<len(B) and k<len(C)):
		min = min(A[i], B[j], C[k])
		max = max(A[i], B[j], C[k])
		# update lowest interval
		if (max-min) < diff:
			min_result = (A[i], B[j], C[k])
			diff = (min - min)
		# difference can't be lower than 0
		if diff == 0: 
			return min_result
		if A[i] == min:
			i += 1
		elif B[i] == min:
			j += 1
		else:
			k += 1
	return min_result
