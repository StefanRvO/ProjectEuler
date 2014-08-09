#!/usr/bin/python

def Factorial(n):
    prod=1
    for i in xrange(2,n+1):
        prod*=i
    return prod


def digitsum(n):
    return sum([int(i) for i in str(n)])



print digitsum(Factorial(100))
