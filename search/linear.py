#!/usr/bin/env python

# O(N)

def find(e, a):
    ''' Returns position or None'''

    for i in range(len(a)):
        if e == a[i]:
            return i
    return None

if __name__ == '__main__':
    print find(1, [0,1,2,3,4,5])
    print find(9, [0,1,2,3,4,5])
