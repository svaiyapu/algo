#!/usr/bin/env python
# best case    : O(N)
# average case : O(N**2)
# worst case   : O(N**2)
# good for mstly sorted data

def isort(a):
    print a
    if len(a) == 1:
        return a

    for i in range(1,len(a)):
        # insert ith element in it's position
        insert(a,i)
    return a

def insert(a,i):
    # note that a[0:i-1] is ordered already
    # thus this is a good algorithm for mostly sorted data
    while i>0 and a[i]<a[i-1]:
        a[i],a[i-1] = a[i-1],a[i]
        i -= 1
        print a

if __name__ == '__main__':
    print isort([3,1,8,5,2,10])
    print isort([10,9,8,76,5])
    print isort([1,2,3,4,5,6])
