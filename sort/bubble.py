#!/usr/bin/env python
# best case    : O(N)
# average case : O(N**2)
# worst case   : O(N**2)
# No good, insertion sort is preferred for the same complexity

def bsort(a):
    print a
    if len(a) == 1:
        return a

    swapped = True
    while swapped:
        swapped = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
                swapped = True
                print a
    return a

if __name__ == '__main__':
    print bsort([3,1,8,5,2,10])
    print bsort([10,9,8,76,5])
    print bsort([1,2,3,4,5,6])
