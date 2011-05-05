#!/usr/bin/env python

def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)

if __name__ == '__main__':
    for i in range(1,10):
        print fib(i)
