"""
In the gas-up problem, nn cities are arranged on a circular road. 
You need to visit all of the nn cities and come back to the starting city. 
A certain amount of gas is available at each city. 
The total amount of gas is equal to the amount of gas required to go around the road once. 
Your gas tank has unlimited capacity. 
Call a city cc ample if you can begin at cc with an empty tank, refill at it, 
	then travel through each of the remaining cities, refilling at each, 
	and return to cc, without running out of gas at any point. 

Given an instance of the gas-up problem, how would you efficiently 
	[i.e. in O(n) time or better] compute an ample city, if one exists?

Assume 20mpg
"""

# Ex. 
# A = [5,30,25,10,10,50,20]
# B = [200,400,600,200,100,900,600]
# => 1 (index of ample city)
# second city (one with 30G gas fillup is amle city)


# solution:
# traverse through cities keeping track of total gas
# (adding as you get to cities and subtracting when traveling to next city)
# allow gas to go negative
# ample_city is city where the amount of gas in take before we refuel at that city is minimum

import sys

def find_ample_city(gallons_for_fill, distances):
	mpg = 20
	gallons_needed = map(lambda x: x/mpg, distances)
	num_cities = len(gallons_for_fill)
	remaining_gas = 0
	min_gal = sys.maxint

	for i in xrange(num_cities):
		remaining_gas += gallons_for_fill[i]
		remaining_gas -= gallons_needed[i]

		if remaining_gas < min_gal:
			min_gal = remaining_gas
			city_pos = (i+1) % num_cities

	# remaining_gas should be >= 0 if ample city exists
	if remaining_gas >= 0:
		return city_pos
	else:
		return -1



A = [5,30,25,10,10,50,20]
B = [200,400,600,200,100,900,600]

print find_ample_city(A,B) # => 1
# second city (one with 30G gas fillup is amle city)

