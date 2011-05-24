#!/usr/bin/env python

def fact(n):
    assert n >= 0
    if n < 2:
        return 1

    return n * fact(n-1)

def fact2(n):
    assert n >= 0
    if n < 2:
        return 1
    
    res = 1
    for i in range(1,n+1):
        res *= i

    return res

if __name__ == '__main__':
    for i in range(10):
        print fact(i)
    for i in range(10):
        print fact2(i)
