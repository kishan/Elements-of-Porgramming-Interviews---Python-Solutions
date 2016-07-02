"""
Given n numbers as well as probablities p0, p1, .... p(n-1) which sum up to 1,
	how would you generate one of n numbers accodring to specified probabilites

Ex. If numbers are 3,5,7,11 and corresponding probabilites are 9/18, 6/18, 2/18, 1/18.
	then in 1,000,000 calls, 3 should appear roughly 500,000 times, 5 should appear 
	roughly 333,333 times, 7 should appear roughly 111,111 times, and 11 should appear
	roughly 55,555 times

Idea: Generate random number between 0 and 1, and select index on number based on 
	what interval range it lands in. 
"""
import random

# space: O(n)
# time: O(n)
def nonUniformRandomNumberGenerator(values, probabilites):
	prob_ranges = [0.0]
	for p in values:
		prev_val = values[len(prob_ranges) - 1]
		new_val = prev_val + p
		prob_ranges.append(new_val)

	d = random.random()

	# search for which range d falls into
	# can use binary search



