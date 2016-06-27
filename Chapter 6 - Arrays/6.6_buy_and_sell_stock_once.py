def max_profit(L):
	if len(L) < 2:
		return 0
	max_profit = 0
	min_price = L[0]
	for cur_price in L:
		max_profit = max(max_profit, cur_price - min_price)
		min_price = min(min_price, cur_price)
	return max_profit