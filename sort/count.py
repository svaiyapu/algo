#!/usr/bin/env python
# O(N) :  to sort a dense population of a small range of unique values

from collections import defaultdict

def cs(a):
    b = defaultdict(int)
    for i in a:
        b[i] += 1

    i = 0
    for j in b.keys():
        while b[j] > 0:
            a[i] = j
            b[j] -= 1
            i += 1

    return a

if __name__ == '__main__':
    print cs([1,2,3,1,2,3,0,1,2,3])
            
