""" 
convert column string to number
Ex. A => 1
Ex. Z => 26
Ex. AA => 27
Ex. AZ => 52
Ex. ZZ => 702 (26*26 + 26)
"""

def col_to_num(column):
	final = 0
	for letter in column:
		final = final*26 + char_value(letter)
	return final


# A => 1
# B => 2
# Z => 26
def char_value(char):
	return ord(char) - ord('A') + 1


print col_to_num("A")
print col_to_num("B")
print col_to_num("AA")
print col_to_num("AZ")
print col_to_num("ZZ")