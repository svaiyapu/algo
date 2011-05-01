#!/usr/bin/env python

# O(1)

def build_hash(a):
    return dict([(v,i) for i,v in enumerate(a)])

def find(e, h):
    ''' Returns position or None'''

    if h.has_key(e):
        return h[e]

    return None

if __name__ == '__main__':
    h = build_hash([3,5,0,10,2,8,1])
    print find(1, h)
    print find(9, h)
