#!/usr/bin/env python

# O(N log N) average case complexity

def merge(a,b):
    r = [None]*(len(a)+len(b))
    i = j = k = 0 # indices into )a, b, r
    while k < (len(a) + len(b)):
        # exhausted a
        if i == len(a):
            while j in range(j,len(b)):
                r[k] = b[j]
                k += 1
                j += 1
            break

        # exhausted b
        if j == len(b):
            while i in range(i,len(a)):
                r[k] = a[i]
                k += 1
                i += 1
            break
                
        # pick the lowest element
        if a[i] <= b[j]:
            r[k] = a[i]
            i += 1
        else:
            r[k] = b[j]    
            j += 1
        k += 1
    print r
    return r
            

def ms(a):
    if len(a) < 2:
        return a

    l = ms(a[0:(len(a)/2)])
    r = ms(a[(len(a)/2):len(a)])
    return merge(l,r)

if __name__ == '__main__':
    print '[8,2,9,5,4,8,7,2,0,1]'
    print ms([8,2,9,5,4,8,7,2,0,1])
