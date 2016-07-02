"""
reverse all words in sentence (don't need to keep original string)

idea:
reverse string
=> then reverse each word

Ex. "this is a sentence" 
	=> "ecnetnes a si siht"
	=> "sentence a is this"

"""

# easy python solution
# def reverse_words(s):
# 	return ' '.join(reversed(my_string.split()))


# 
def reverse_words(s):
	s = s[::-1]

	final = ""
	word = ""
	for i in xrange(len(s)):
		if s[i] == " ":
			final = final + " " + word[::-1]
			word = ""
		else:
			word += s[i]

	final = final + " " + word[::-1]
	i = 0
	while (i <= len(s) and s[i] == " "):
		i += 1
	first_non_space = i + 1
	return final[first_non_space:]
	

print reverse_words("this is a sentence ")
