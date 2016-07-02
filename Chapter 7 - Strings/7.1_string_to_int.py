__author__ = 'Marie Hoffmann'

'''
    Convert string representing signed integer to integer without using library functions.
'''

def stringToInt(s):
    result = 0
    if len(s) == 0 or len(s) == 1 and (ord(s[0]) < 48 or ord(s[0]) > 57):
        return 0
    sign = -1 if s[0] == '-' else 1
    if s[0] == '-' or s[0] == '+':
        s = s[1:]
    for i in range(len(s)):
        result = 10*result + ord(s[i]) - 48
    return result*sign


print stringToInt('123')
print stringToInt('-123')
print stringToInt('+3678')
print stringToInt('+0')