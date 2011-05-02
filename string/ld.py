#!/usr/bin/env python
# O(N*M)
import pprint

def ld(s, t):
    '''
        Computes Levenshtein distance between souce and target strings
    '''
    if s == t:
        return 0
    if t in s or s in t:
        return abs(len(s) - len(t))

    d = [None] * (len(s)+1)
    for i in range(len(s)+1):
        d[i] = [None] * (len(t)+1)
        d[i][0] = i

    for j in range(len(t)+1):
        d[0][j] = j


    for j in range(1,len(t)+1):
        for i in range(1,len(s)+1):
            si = i-1
            tj = j-1
            if s[si] == t[tj]:
                d[i][j] = d[i-1][j-1] # same distance as before
            else:
                d[i][j] = min(
                            d[i-1][j] + 1,    # deletion
                            d[i][j-1] + 1,    # addition
                            d[i-1][j-1] + 1   # replacement
                            )


    return d[i][j]

if __name__ ==  '__main__':
    print ld('this', 'this')
    print ld('', '')
    print ld('', 'this')
    print ld('this', '')
    print ld('is', 'this')
    print ld('this', 'is')
    print ld('this', 'thit')
