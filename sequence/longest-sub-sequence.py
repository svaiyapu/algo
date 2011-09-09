#!/usr/bin/env python

def lss(a):
    '''Returns longest sum sub sequence, relies on tuple sorting (max function)'''
    if not a:
        return a
    # (sum, length, start, end)
    s,l,i,j = max([(sum(a[i:j]),j-i,i,j) for i in range(len(a)) for j in range(len(a)+1) if j > i])
    return a[i:j]

if __name__ == '__main__':
    assert([] == lss([]))
    assert([1] == lss([1]))
    assert([0,1,2,3] == lss([-3,-2,-1,0,1,2,3]))
    assert([4,-2,-1,0,1,2,3] == lss([4,-2,-1,0,1,2,3]))
    assert([0,0,0,10] == lss([-10,0,0,0,10,-10]))
