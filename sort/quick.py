#!/usr/bin/env python

# O(N log N) - Average 
# O(N**2)    - Worst case

def partition(a, l, r, p):
    v = a[p]
    a[p],a[r] = a[r],a[p] # store away pivot value
    si = l
    # swap lower values compared to pivot resulting in a new
    # pivot postion
    for i in range(l, r):
        if a[i] < v:
            a[i], a[si] = a[si], a[i]
            si += 1
    a[si],a[r] = a[r], a[si] # store back pivot value
    # now we have <pivot, pivot, >pivot values
    return si

def qs(a, l, r):
    if len(a) < 2:
        return a

    if (l > r):
        return a

    if (r > l):
        p = (l + r)/2
        pn = partition(a, l, r, p)
        qs(a, l, pn-1)
        qs(a, pn+1, r)
    
    return a

if __name__ == '__main__':
    a = [3,1,10,9,0,4,8,2,1]
    print qs(a, 0, len(a)-1)
