"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
A valid IP address must be in the form of A.B.C.D, where A,B,C and D are numbers from 0-255. 
The numbers cannot be 0 prefixed unless they are 0. (Ex "0" is valid but "00" and "01" are not)
Example:
Given “25525511135”,
return [“255.255.11.135”, “255.255.111.35”]. (Make sure the returned strings are sorted in order)



Idea:
Brute force works here.
Essentially you have to place 3 dots in the given string.
Try out all the possible combinations for the 3 dots.
We can reduce number of placements considered by spacing the periods 1 to 3 places
    apart and stopping as soon as substring is not valid
"""

def restoreIpAddresses(s):
    result = []
    for i in xrange(1,4):
        if not(i<len(s)): pass
        first = s[:i]
        if isValid(first):
            for j in xrange(1,4):
                if not(i+j<len(s)): pass
                second = s[i:i+j]
                if isValid(second):
                    for k in xrange(1,4):
                        if not(i+j+k<len(s)): pass
                        third = s[i+j:i+j+k]
                        fourth = s[i+j+k:]
                        if isValid(third) and isValid(fourth):
                            result.append(first+"."+second+"."+third+"."+fourth)
    return result


def isValid(s):
    if len(s) == 0 or len(s) > 3:
        return False
    if s[0] == "0":
        if len(s) > 1:
            return False
        else:
            return True
    return int(s) >= 0 and int(s) <= 255



print restoreIpAddresses("19216811")
# => ['1.92.168.11', '19.2.168.11', '19.21.68.11', '19.216.8.11', '19.216.81.1', '192.1.68.11', '192.16.8.11', '192.16.81.1', '192.168.1.1']
print restoreIpAddresses("19256811")
# => ['19.25.68.11', '192.5.68.11', '192.56.8.11', '192.56.81.1']