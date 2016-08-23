"""
Majority Element: A majority element in an array A[] of size n is an element 
	that appears more than n/2 times (and hence there is at most one such element).

Write a function which takes an array and emits the majority element (if it exists), 
	otherwise prints NONE as follows:

Ex.
[3 3 4 2 4 4 2 4 4] => 4 
[3 3 4 2 4 4 2 4] => NONE


SOLUTION:
Above algorithm loops through each element and maintains a count of a[maj_index], 
If next element is same then increments the count, 
if next element is not same then decrements the count, 
and if the count reaches 0 then changes the maj_index to 
the current element and sets count to 1.

First Phase algorithm gives us a candidate element. 
In second phase we need to check if the candidate is really a majority element. 
Second phase is simple and can be easily done i



Example:
A[] = 2, 2, 3, 5, 2, 2, 6
Initialize:
maj_index = 0, count = 1 –> candidate ‘2?
2, 2, 3, 5, 2, 2, 6

Same as a[maj_index] => count = 2
2, 2, 3, 5, 2, 2, 6

Different from a[maj_index] => count = 1
2, 2, 3, 5, 2, 2, 6

Different from a[maj_index] => count = 0
Since count = 0, change candidate for majority element to 5 => maj_index = 3, count = 1
2, 2, 3, 5, 2, 2, 6

Different from a[maj_index] => count = 0
Since count = 0, change candidate for majority element to 2 => maj_index = 4
2, 2, 3, 5, 2, 2, 6

Same as a[maj_index] => count = 2
2, 2, 3, 5, 2, 2, 6

Different from a[maj_index] => count = 1

Finally candidate for majority element is 2.

First step uses Moore’s Voting Algorithm to get a candidate for majority element.

2. Check if the element obtained in step 1 is majority
"""






