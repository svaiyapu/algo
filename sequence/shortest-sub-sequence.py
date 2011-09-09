#!/usr/bin/env python

def sss(a):
    '''Returns shorteest sum sub sequence with maximum sum, 
       relies on tuple sorting (max function)'''
    if not a:
        return a
    # (sum, length, start, end)
    s,l,i,j = max([(sum(a[i:j]),len(a)-(j-i),i,j) for i in range(len(a)) for j in range(len(a)+1) if j > i])
    return a[i:j]

if __name__ == '__main__':
    assert([] == sss([]))
    assert([1] == sss([1]))
    assert([1,2,3] == sss([-3,-2,-1,0,1,2,3]))
    assert([4,-2,-1,0,1,2,3] == sss([4,-2,-1,0,1,2,3]))
    assert([-10,0,0,0,10,-10] == lss([10]))
