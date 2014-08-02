#!/usr/bin/python


def isSquare(num):
    if num<=0:
        return False
    square=num**0.5
    if square==int(square):
        return True
    return False
squares=[]
for i in range(1,100):
    squares.append(i**2)
minimum=9999999999999
for i in xrange(1,1000000):
    a=i**2
    for j in xrange(1,i):
        c=j**2
        f=a-c
        if not isSquare(f):
            continue
        for l in xrange(1,j):
            d=l**2
            e=a-d
            b=c-e
            if not isSquare(e):
                continue
            if not isSquare(b):
                continue
            x=(a+b)/2.
            y=(e+f)/2.
            z=(c+d)/2.
            if not x>y:
                continue
            if
            if x+y+z<minimum:
                minimum=x+y+z
                print "New Record",x,y,z,x+y+z
