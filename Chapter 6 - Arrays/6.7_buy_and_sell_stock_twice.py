# brute force: examine all combos -> O(n^4)

# Ex. [12, 11, 13, 9, 12, 8, 14, 13, 15]
# profit_list_on_before_i = [0,0,2,2, 3,3,6,6,7]
# profit_list_after_i =   [7,7,7,7,7, 7,2,2,0]
# final profits =		  [7,7,7,9,9,10,5,8,6]
# max profit = 

def max_profit(L):
	if len(L) < 2:
		return 0
	max_profit = 0
	# For each day, find the max profit with single buy and sell before or on Day i
	profit_list_on_before_i = []
	for cur_price in L:
		min_price = min(min_price, cur_price)
		max_profit = max(max_profit, cur_price - min_price)
		profit_list_on_before_i.append(max_profit)

	# backwards phase. 
	# For each day, find the max profit with single buy and sell after Day i
	profit_list_after_i = [0] * len(L)
	max_price_so_far = L[len(L)-1]
	for i in xrange(len(L)-1, -1, -1):
		max_price_so_far = max(max_price_so_far, L[i])
		profit_list_after_i[i] = (max_price_so_far - L[i])

	final_max = 0
	for i in xrange(1,len(L)):
		profit = profit_list_on_before_i[i-1] - profit_list_after_i[i]
		final_max = max(final_max, profit)

		
	return final_max