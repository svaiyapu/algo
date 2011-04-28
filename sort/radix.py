#!/usr/bin/env python
#
# O(N)
# 

from collections import defaultdict

def bucket(a,i):   
    print a
    b = defaultdict(list)
    for e in a:
        f = "%03d" % e
        b[f[i]].append(e)
    return b

def rs(a):
    # order by LSD
    for i in range(3)[::-1]:
        r = []
        b = bucket(a,i)
        for i in range(10):
            if b.has_key(str(i)):
                r += b[str(i)]
        a = r
    return a

if __name__ == '__main__':
    print rs([953, 9, 4, 325, 0, 72])
