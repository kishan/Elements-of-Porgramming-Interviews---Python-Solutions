"""
given an array of letters, replace each 'a' with 2 'd's and delete all 'b's
you are given a variable size that represents the number of characters to consider
assume the array has sufficient space to fit final result
you don't care about that values after 'size' number of chars

Idea:

"""

def replace_and_remove(L, size):
	write_index = 0
	a_count = 0

	# remove all b from array
	for i in xrange(size):
		if L[i] != "b":
			L[write_index] = L[i]
			write_index += 1
		if L[i] == "a":
			a_count += 1

	cur_index = write_index - 1
	write_index = write_index + a_count - 1
	final_size = write_index + 1

	# starting from back, write each char to back, replacing 'a' with 2 'd's
	while (cur_index >= 0):
		if L[cur_index] == "a":
			L[write_index] = "d"
			L[write_index - 1] = "d"
			write_index -= 2
		else:
			L[write_index] = L[cur_index]
			write_index -= 1
		cur_index -= 1

	return L



print replace_and_remove(["a","b","a","c",None], 4) 
# => ['d', 'd', 'd', 'd', 'c']
print replace_and_remove(["a","c","d","b","b","c","a"], 7)
# => ['d', 'd', 'c', 'd', 'c', 'd', 'd']


