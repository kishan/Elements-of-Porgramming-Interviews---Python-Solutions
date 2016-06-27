# Ex. [0,1,2,3] => [0,1,3,2]
# Ex. [0,1,3,2] => [0,2,1,3]
# Ex. [0,2,1,3] => [0,2,3,1]
# Ex. [3,2,1,0] => None
"""
Following is the algorithm for finding the next greater number.
I) Traverse the given number from rightmost digit, keep traversing till you 
        find a digit which is smaller than the previously traversed digit. 
        For example, if the input number is “534976”, we stop at 4 because 4 is 
        smaller than next digit 9. If we do not find such a digit, 
        then output is “Not Possible”.

II) Now search the right side of above found digit ‘d’ for the smallest digit 
        greater than ‘d’. For “534976″, the right side of 4 contains “976”. 
        The smallest digit greater than 4 is 6.

III) Swap the above found two digits, we get 536974 in above example.

IV) Now sort all digits from position next to ‘d’ to the end of number. 
        The number that we get after sorting is the output. 
        For above example, we sort digits in bold 536974. 
        We get “536479” which is the next greater number for input 534976.
        *** don't need to sort...since in descending order, we can reverse instead
"""

def find_next(s):
    n = len(s)

    # I) Start from the right most digit and find the first digit that is
    # smaller than the digit next to it.
    i = n-1
    while i > 0:
        if s[i-1] < s[i]:
            break
        i -= 1

    if i == 0:
        return None

    # II) Find the smallest digit on right side of (i-1)'th digit that is
    # greater than number[i-1]
    x = s[i-1]
    smallest = i;
    for j in xrange(i+1, n):
        if (s[j] > x and s[j] < s[smallest]):
            smallest = j

    # III) Swap the above found smallest digit with number[i-1]
    (s[smallest], s[i-1]) = (s[i-1], s[smallest])
 
    # IV) Sort the digits after (i-1) in ascending order
    first_part = s[:i]
    second_part = s[i:]
    return first_part + second_part[::-1]


s1 = [0,1,2,3]
s2 = [0,1,3,2]
s3 = [0,2,1,3]
s4 = [0,2,3,1]
s10 = [3,2,1,0]
print find_next(s10)