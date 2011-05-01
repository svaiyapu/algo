#!/usr/bin/env python
# O(N+M)

def SpecialSort(a, b, n, m):
    """
        Inserts pre-sorted array 'a' of 'n' elements into pre-sorted array 'b' of 'm+n' 
        elements
    """
    assert len(a) > 0
    assert len(b) > 0
    assert n > 0 and n == len(a)
    assert m > 0 and m == len(b)
    
    # extend list 'b' with 'n' elements
    for k in range(n):
        b.append(None)

    k = n+m-1
    j = m-1
    i = n-1
    while k > -1:
        # exhausted a, we are done
        if i == -1:
            k = -1
            next
            
        # exhausted b, copy over remaining a
        if j == -1:
            for l in range(i+1)[::-1]:
                b[k] = a[l]
                k -= 1
            next

        # pick max(a,b), store in b and adjust pointer where the value is picked from
        if j > -1 and i > -1:
            if a[i] > b[j]:
                b[k] = a[i]
                i -= 1
            else:
                b[k] = b[j]
                j -= 1

        k -= 1

    assert len(b) == m+n
    return b
            
if __name__ == "__main__":
    # tests
    print SpecialSort([1,2,3], [2,5], 3, 2)
    print SpecialSort([1,2,5], [2,3], 3, 2)
    print SpecialSort([1], [1], 1, 1)
    print SpecialSort([0,6,7,8,9], [1,2,3,4,5], 5, 5)
    print SpecialSort([0,6], [1,2,3,4,5], 2, 5)
    print SpecialSort([6,7,8,9], [0,1,2,3,4,5], 4, 6)
    print SpecialSort([1,2,3,4], [5,6,7,8,8], 4, 5)
    print SpecialSort([0,2,4,6,8], [1,3,5,7,9], 5, 5)
