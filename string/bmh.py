#!/usr/bin/env python
"""
  Boyer-Moore-Horspool
  Average : Linear : O(N) - Length of haystack
  Worst : O(N*M) - Length of haystack * Length of Needle
"""
import string

def bmh(h, n):
    # populate the jump/skip table 
    j = {}
    for s in string.printable:
        j[s] = len(n)

    # for the characters in needle adjust the jump value
    # except the last character
    for i in range(len(n) - 1):
        j[n[i]] = len(n) - 1 - i

    s = len(n) - 1 # current start index (length of needle)
    while s < len(h):
        l =  len(n) - 1
        c = s
        while l >= 0 and h[c] == n[l]:
            if l == 0: # match found
                return c
            c -= 1
            l -= 1
        
        # match not found, jump based on the last start position
        s += j[h[s]]
        
    return None

if __name__ == '__main__':
    p = bmh('haysteckneedhaystackabneedlzhaystack', 'needlz')
    print p
    p = bmh('haystackneedhaystackneedlehaystack', 'e')
    print p
    p = bmh('imonkeypantspantsmonkeyblahblah', 'kid')
    print p
