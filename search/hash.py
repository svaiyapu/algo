#!/usr/bin/env python

# O(1)

def build_hash(a):
    return dict([(v,i) for i,v in enumerate(a)])

def find(e, a):
    ''' Returns position or None'''

    h = build_hash(a)

    if h.has_key(e):
        return h[e]

    return None

if __name__ == '__main__':
    print find(1, [0,1,2,3,4,5])
    print find(9, [0,1,2,3,4,5])
