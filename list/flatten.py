#!/usr/bin/env python

# Flatten nested lists

def flatten(a, stack=None):
    ''' Using accumulator'''
    if not stack:
        stack = []
    for e in a:
        if isinstance(e, list):
            flatten(e, stack)
        else:
            stack.append(e)
    return stack

def flatten3(a):
    ''' Using yield'''
    for e in a:
        if isinstance(e, list):
            for e2 in flatten3(e):
                yield e2
        else:
            yield e

def flatten2(a):
    ''' In place, using slice assignment '''
    i = 0
    while i < len(a):
        while isinstance(a[i], list):
            if len(a[i]) == 0:
                a.pop(i)
                i -= 1
                break
            else:
                a[i:i+1] = a[i]
        i += 1
    return a

print flatten([1,2,3,[4,5],6,7,[8,9]])
print flatten([1,2,3,[4,5],6,7,[8,9]])
print flatten2([1,2,3,[4,5],6,7,[8,9]])
print flatten2([1,2,3,[[4,5]],6,[],7,[8,9]])
print list(flatten2([1,2,3,[[4,5]],6,[],7,[8,9]]))
print list(flatten3([1,2,3,[4,5],6,7,[8,9]]))
