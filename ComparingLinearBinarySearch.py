# File: ComparingLinearBinarySearch.py
# Student: Gaytri Riya Vasal
# UT EID: grv377
# Course Name: CS303E
# 
# Date Created: 11/2/2021
# Date Last Modified: 11/5/2021
# Description of Program: The following program will compare the results of linear and binary search.

import random

import math

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

def main():
    lst = [x for x in range(1000)]
    random.shuffle(lst)

    counter = 0
    
    for i in range(10):
        index = linearSearch(lst, random.choice(lst))
        counter += index + 1

    average10 = counter / (10)

    counter = 0

    for i in range(100):
        index = linearSearch(lst, random.choice(lst))
        counter += index + 1
    
    average100 = counter / (100)

    counter = 0

    for i in range(1000):
        index = linearSearch(lst, random.choice(lst))
        counter += index + 1
    
    average1000 = counter / (1000)

    counter = 0

    for i in range(10000):
        index = linearSearch(lst, random.choice(lst))
        counter += index + 1
    
    average10000 = counter / (10000)

    counter = 0

    for i in range(100000):
        index = linearSearch(lst, random.choice(lst))
        counter += index + 1
    
    average100000 = counter / (100000)

    print()
    print("Linear search:")
    print("  Tests: 10       Average probes:", average10)
    print("  Tests: 100      Average probes:", average100)
    print("  Tests: 1000     Average probes:", average1000)
    print("  Tests: 10000    Average probes:", average10000)
    print("  Tests: 100000   Average probes:", average100000)

    lst = [x for x in range(1000)]

    counter = 0
    
    for i in range(1000):
        index, count = binarySearch(lst, random.choice(lst))
        counter += count

    binaryaverage1000 = counter / (1000)

    print("Binary search:")
    print("  Average number of probes:", binaryaverage1000)
    print("  Differs from log2(1000) by:", (math.log2(1000) - binaryaverage1000))
    print()
    
main()
