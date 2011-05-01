#!/usr/bin/env python

# O(log N)
# Collection is ordered

def find(e, a):
    ''' Returns position or None'''

    if len(a) == 0:
        return None

    i = len(a)/2
    print i, a

    if e == a[i]:
        return i
    
    if e < a[i]:   
        return find(e, a[0:i])
    else:
        return find(e, a[i+1:len(a)])
    
    return None

if __name__ == '__main__':
    print find(1, [0,1,2,3,4,5])
    print find(9, [0,1,2,3,4,5])
