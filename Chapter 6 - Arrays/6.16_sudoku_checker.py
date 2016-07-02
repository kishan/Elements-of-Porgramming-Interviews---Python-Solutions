"""
Check whether an n x n 2D array representing a partially completed Sudoku is valid.
specifically check that no row, column or sqrt(n) X sqrt(n) 2D subarray contains duplicates.
A 0 value in the 2D array indicates blank, every other entry is in [1,n]

Idea: solution is straight forward and just involves checking for duplicates
"""
import math

# space: O(n)
# time: O(n^2)
def SudokuChecker(S):
	def HasDuplicates(startRow, endRow, startCol, endCol, sudokuBoard):
		found = {}
		for i in xrange(startRow, endRow):
			for j in xrange(startCol, endCol):
				value = sudokuBoard[i][j]
				if value != 0 and value in found:
					return True
				else:
					found[value] = 1
		return False

	size = len(S)

	# check columns
	for i in xrange(size):
		if HasDuplicates(i, i+1, 0, size, S):
			return False

	# check rows
	for j in xrange(size):
		if HasDuplicates(0, length, j, j+1, S):
			return False

	regionSize = int(math.sqrt(size))

	# check each box region
	for i in xrange(regionSize):
		for j in xrange(regionSize):
			if HasDuplicates(i*regionSize, 
							i*regionSize+regionSize, 
							j*regionSize, 
							j*regionSize+regionSize,
							S):
				return False

	return True

