"""
Find the n'th term in Look-and-say (Or Count and Say) Sequence. The look-and-say sequence is the sequence of below integers:
1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...


How is above sequence generated?
n'th term in generated by reading (n-1)'th term.

The first term is "1"

Second term is "11", generated by reading first term as "One 1" 
(There is one 1 in previous term)

Third term is "21", generated by reading second term as "Two 1"

Fourth term is "1211", generated by reading third term as "One 2 One 1" 

and so on...
"""

# find n'th look_and_say number
def look_and_say(n):
	s = "1"
	for i in xrange(n):
		s = nextNumber(s)
	return s

# www.rosettacode.org
def nextNumber(number):
    result = ""
 
    repeat = number[0]
    number = number[1:]+" "
    times = 1
 
    for actual in number:
        if actual != repeat:
            result += str(times)+repeat
            times = 1
            repeat = actual
        else:
            times += 1

    return result
 
 

for i in xrange(10):
	print look_and_say(i)