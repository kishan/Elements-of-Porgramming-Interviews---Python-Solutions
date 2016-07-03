def sinusoidal(s):
	result = ""

	# // first row: s[1], s[5], s[9], ...
	for i in xrange(1, len(s), 4):
		result += s[i]

	# second row: s[0], s[2], s[4], s[6]. ...
	for i in xrange(0, len(s), 2):
		result += s[i]

	# third row: s[3], s[7], s[11], ...
	for i in xrange(3, len(s), 4):
		result += s[i]

	return result


print sinusoidal("Hello World")
# => "e lHloWrdlo"
