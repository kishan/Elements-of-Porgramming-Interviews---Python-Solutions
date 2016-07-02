"""
Check if string is palindrome only considering numbrs and letters (insensitive of case)
Ex. a man, a plan, a canal, a Panama
"""
import string

# space: O(1)
# time: O(n)
def is_palindrone(s):
	allowed = string.letters + string.digits
	i = 0
	j = len(s) - 1
	while (i < j):
		while (s[i] not in allowed and i < j):
			i += 1
		while (s[j] not in allowed and i < j):
			j -= 1
		if s[i].lower() != s[j].lower():
			return False
		i += 1
		j -= 1
	return True


print is_palindrone("a man, a plan, a canal, Panama")