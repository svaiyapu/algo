#!/usr/bin/env python

def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

def fib2(n):
    a,b = 1,1
    for i in range(1,n):
        a,b = b,a+b
    return a

if __name__ == '__main__':
    for i in range(1,10):
        print fib(i)
    for i in range(1,10):
        print fib2(i)
