# given a list of intervals, find min number of points needed to cover all intervals

# Ex. [[0,3],[2,6],[3,4],[6,9]] => [3,6]
# Ex. [[1,2],[2,3],[3,4],[2,3],[3,4],[4,5]] => [2,4]

# solution:
# sort intervals by ending time
# select the first inerval's right endopint
# iterate through the intervals, looking for the first one not covered by this right endpoint
# as soon as such an interval is found, select its right endpoint and continue the iteration


def compare_second_val(item1, item2):
    if item1[1] < item2[1]:
        return -1
    elif item1[1] > item2[1]:
        return 1
    else:
        return 0

# O(nlog(n)) to sort and O(n) after
def min_points(L):
	L = sorted(L, cmp = compare_second_val)
	last_visit_time = L[0][1]
	final = [last_visit_time]
	for interval in L:
		if interval[0] > last_visit_time:
			last_visit_time = interval[1]
			final.append(last_visit_time)

	return final