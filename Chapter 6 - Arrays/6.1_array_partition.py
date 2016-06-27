# smaller represents first index of equal value
# equal represents current index
# so if equal index comes across value that is equal to A[i], then 
#	it will switch values with "smaller" index
def partition(A, i):
	smaller = 0
	equal = 0
	larger = len(A) - 1
	while (equal < larger):
		if A[equal] < A[i]:
			swap(A[smaller], A[equal])
			smaller += 1
			equal += 1
		elif A[equal] > A[i]:
			swap(A[larger], A[equal])
			larger += 1
		else:
			equal += 1
