"""
convert roman numeral to int
"""

# iterate from left to right
def romanToInt(self, A):
        D = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        prev = None
        final = 0
        for c in A:
            cur = D[c]
            final += cur
            if cur > prev and prev is not None:
                final -= prev*2
            prev = cur
        return final


# iterate from right to left
# probably simpler solution
def romanToInt(self, A):
        D = { "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1 }
        final = A[len(A)-1]
        for i in xrange(len(A)-2, -1, -1):
        	cur_int = D[A[i]]
        	int_to_right = D[A[i+1]]

        	if cur_int < int_to_right:
        		final -= cur_int
        	else:
        		final += cur_int
        return final