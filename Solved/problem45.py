#!/usr/bin/python

def TriangleNumber(n):
    return n*(n+1)/2
def PentagonalNumber(n):
    return n*(3*n-1)/2
def HexagonalNumber(n):
    return n*(2*n-1)
def TriangleNumberinv(n):
    return -(1./2)+(1./2)*((1+8*n)**0.5)
def PentagonalNumberinv(n):
    return 1./6+1./6*((1+24*n)**0.5)
def HexagonalNumberinv(n):
    return 1/4.+1./4*((1+8*n)**0.5)
def isPentagonalNumber(n):
    inv=PentagonalNumberinv(n)
    if int(round(inv,5))== round(inv,5):
        return True
    return False
def isHexagonalNumber(n):
    inv=HexagonalNumberinv(n)
    if int(round(inv,5))== round(inv,5):
        return True
    return False
def isTriangleNumber(n):
    inv=TriangleNumberinv(n)
    if int(round(inv,5))== round(inv,5):
        return True
    return False
    
i=0
while(True):
    i+=1
    Hexagonalnum=HexagonalNumber(i)
    if isPentagonalNumber(Hexagonalnum):
        if isTriangleNumber(Hexagonalnum):
            print Hexagonalnum,"triangle=",int(TriangleNumberinv(Hexagonalnum)),"Pentagonal=",int(PentagonalNumberinv(Hexagonalnum)),"Hexagonal=",i
