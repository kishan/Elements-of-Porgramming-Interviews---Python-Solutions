"""
enumerate all primes up to n
Ex. 18 => [2,3,5,7,11,17]
"""

# better solution in book other than this one
def enumerate_primes(M):
	"""
	Use the Sieve of Eratosthenes to returns the 
	sum of h_E(p) over all primes p<M.
	
	Here M is assumed to be an integer >= 2.
	"""
	# Create the index list. Python indexes from 0.
	index_list = [True]*M
	# Set index_list[0] and index_list[1] to False,
	# since 0 and 1 are by definition not prime
	index_list[0] = False
	index_list[1] = False
	
	bound = (float(M))**(1.0/2)
	p = 2
	while p<bound:
		# Small optimization: only need to start index
		# iteration at p^2, since all composites less
		# than that will already have been crossed off
		i = p**2
		while i<M:
			index_list[i]=False
			i += p
		# Find the next prime
		p += 1
		while index_list[p]==False:
			p += 1
	# index_list will now index the primes up to M
	print index_list
	# Sum computing time. Enumerate over those n for
	# which index_list[n] is True
	final_list = []
	n = int(2)
	while n < M:
		# This check is much faster than testing for
		# primality
		if index_list[n]==True:
			final_list.append(n)
		n += 1
	# Done
	return final_list

print enumerate_primes(18)