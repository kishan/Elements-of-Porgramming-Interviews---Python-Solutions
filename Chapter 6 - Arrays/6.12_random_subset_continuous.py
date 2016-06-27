"""
SAMPLE ONLINE DATA

maintain random subset of size k given continous stream of numbers (A given as iterator)

Suppose we have read the first n numbers, and have a subset of k of them
When we read the (n+1)th number, it should belong to the subset with probability k/(n+1)
If we choose one of the numbers in the exisiting subset uniformly randomly to remove, 
    the resulting collection will be a random subset of n+1 numbers
"""
import random


 # Assumption: there are at least k elements in the stream.
 # A is iterator
def random_subset_continuous(A, k):
  runningSample = []

  # Stores the first k elements.
  for i in xrange(k):
    runningSample.append(next(A))

  # Have read the first k elements.
  numSeenSoFar = k
  done = False
  while (not done):
    try:
      x = next(A)
      numSeenSoFar += 1
      # Generate a random number in [0, numSeenSoFar], and if this number is in
      # [0, k - 1], we replace that element from the sample with x.
      idxToReplace = random.randint(0, numSeenSoFar)
      print x, idxToReplace
      if idxToReplace < k:
        runningSample[idxToReplace] = x
    except StopIteration:
      done = True

  return runningSample


A = range(10)
A_iter = iter(A)
print random_subset_continuous(A_iter, 5)


