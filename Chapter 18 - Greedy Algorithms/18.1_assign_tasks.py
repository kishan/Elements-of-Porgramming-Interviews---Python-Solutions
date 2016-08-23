# design an alogirhtms that takes as input a set of tasks and returns an optimum assignment
# given list of ints representing how long a task takes
# each worker must be assigned two tasks
# assign two tasks to each worker
# find assignments to workers that results in minimum time to finish all tasks

# Ex. [5,2,1,6,4,4] => [(1,6), (2,5), (4,4)]  (min assignments will take 8 hours)


# solution: 
# sort set of task durations & pair shortest, 2nd shortest, 3rd shortest
# 	with longest, 2nd longest, 3rd longest
def assign_tasks(L):
	L.sort()
	i = 0
	j = len(L) - 1
	final = []
	while (i < j):
		tuple = (L[i], L[j])
		final.append(tuple)
		i += 1
		j -= 1
	return final