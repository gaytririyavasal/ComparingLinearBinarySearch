
PROJECT DESCRIPTION AND GUIDELINES PROVIDED ON ASSIGNMENT INSTRUCTIONS

Your task is to compare the performance of linear and binary search. "Comparing" means seeing on average how many probes (comparisons) are made as you search a list and how closely that average matches the "expected" value. For linear search, the expected number of probes is approximately half the length of the list, if the item is present, and the entire length of the list, if the item is not present. Think about why that should be the case. For binary search, the expected number of probes is approximately the logarithm base 2 of the length of the list, whether the item is present or not. You will be conducting some experiments to see whether these estimates are accurate. Note that in these experiments, the value searched will always be in the list because of the way we set up the problem.

Below is some slightly modified code for Linear Search and Binary Search:

def linearSearch( lst, key ):
    """ Search for key in unsorted list lst.  Note that
        the index + 1 is also the number of probes. """
    for i in range( len(lst) ):
        if key == lst[i]:
            return i
    return -1

def binarySearch( lst, key ):
    """ Search for key in sorted list lst. Return
        a pair containing the index (or -low - 1)
        and a count of number of probes. """
    count = 0
    low = 0
    high = len(lst) - 1
    while (high >= low):
        count += 1
        mid = (low + high) // 2
        if key < lst[mid]:
            high = mid - 1
        elif key == lst[mid]:
            return (mid, count)
        else:
            low = mid + 1
    # Search failed
    return (-low - 1, count)

Notice that the number of probes (comparisons) for linear search is the index returned plus 1. I.e., if you found the item at location 423, then you've looked at 424 items. For binary search, you have to keep track of the number of probes. I've modified the binarySearch code to return a tuple (pair) including the index and the count.

To deal with the tuple returned by binary search, you can just do the following:

    index, count = binarySearch( lst, key )

where index and count are just two variables where you want to store the results. This code will put the two values returned by binarySearch into those two variables.

Your assignment has two parts. Part 1 is to generate a list of the values from 0 to 999, shuffle the list (using the random.shuffle method) and then perform linear search n times on random keys (values) selected in the range 0 to 999. Only generate the list once, and search it for n randomly generated keys. Keep track of the number of probes for each search and find the average over all n experiments. Be sure to reset the counter for each experiment (but always use the same list). You'll do this for n equal to each of the following: 10, 100, 1000, 10000, 100000. Report those averages. (Note that the search should always succeed because the list contains all of the values from 0 to 999, by construction.) Ideally, the bigger the value of n, the closer you should get to the expected value of 500. (If that doesn't happen it could be because the selection of keys is not truly random or the shuffle may not be perfect. That shouldn't be the case if you're using the right Python functions. So if it does happen, check your code. Note that you don't have to round your answers.

For Part 2, you'll do a similar experiment for binary search. For this, you'll need a sorted list; generate the list of values from 0 to 999 in order (i.e., [0, 1, 2, ..., 999]). You only need to generate this list once; don't regenerate it for each experiment. Notice that this list is already sorted. Perform binary search 1000 times on random keys selected in the range 0 to 999. Average the number of probes per search. It should be close to the logarithm (base 2) of 1000. (You can get that value as follows: import math and use the function math.log2(1000).) Print out the average and the difference between the log base 2 of 1000 and your average. You do not need to round any of your answers.

For example, here are two different runs of the program:

> python ComparingLinearBinarySearch.py
Linear search:
  Tests: 10       Average probes: 435.7
  Tests: 100      Average probes: 518.54
  Tests: 1000     Average probes: 510.41
  Tests: 10000    Average probes: 504.9113
  Tests: 100000   Average probes: 501.46064
Binary search:
  Average number of probes: 9.026
  log2(1000): 9.965784284662087
  Differs from log2(1000) by: 0.9397842846620872
> python ComparingSearchAlgorithms.py
Linear search:
  Tests: 10       Average probes: 459.8
  Tests: 100      Average probes: 505.08
  Tests: 1000     Average probes: 515.144
  Tests: 10000    Average probes: 492.3511
  Tests: 100000   Average probes: 500.64277
Binary search:
  Average number of probes: 8.959
  log2(1000): 9.965784284662087
  Differs from log2(1000) by: 1.0067842846620874
> 

Your output should look like this, except that your numbers will be different.

