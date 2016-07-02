__author__ = 'Marie Hoffmann ozymandiaz147@googlemail.com'

'''
    Write program that receives a string representing an integer of base b1 and returns a string
    representing the same number in base b2 where 2 <= b1, b2 <= 16.

    Ex. "615" b1 = 7, b2 = 13
    Decimal value = 306 (6*7^2 + 1*7 + 5)
    Least significant digit of result is is 306 mod 13 = 7. 
    We continue with 306/13 = 23
    The next digit is 23 mod 13 = 10, which we denote by 'A'
    We continue with 23/13 = 1. Since 1 mod 13 = 1 and 1/13 = 0, the final digit is 1, 
        and the overall result is 1 and the overall result "1A7"
'''

import math

def base_conversion(s, b1, b2):
    if s[0] == "-":
        sign = "-"
        s = s[1:]
    else:
        sign = ""
    # convert to decimal
    d = 0
    exponent = len(s)-1
    for str_ in s:
        val = convert_string_to_dec(str_)
        d += (b1**exponent)*val
        exponent -= 1
    return sign + construct_from_base(d, b2)



def construct_from_base(n, base):
    if n < base:
        return convert_dec_to_string(n)
    return construct_from_base(n/base, base) + convert_dec_to_string(n%base)

def convert_string_to_dec(s):
    if ord(s) >= ord("0") and ord(s) <= ord("9"):
        return ord(s) - ord("0")
    else:
        return ord(s) - ord("A") + 10

# Ex. 4 => "4"
# Ex. 11 => "B"
def convert_dec_to_string(n):
    if n >= 10:
        return chr(ord("A") + n - 10)
    else:
        return chr(ord("0") + n)






# all equal to 27
print base_conversion('11011', 2, 3)
print base_conversion('1000', 3, 2)
print base_conversion('11011', 2, 16)
print base_conversion('-01B', 16, 8)


