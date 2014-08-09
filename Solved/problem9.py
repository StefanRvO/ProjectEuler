#!/usr/bin/python
import sys
def isPythagoreanTrip(a,b,c):
    if a**2+b**2==c**2:
        return True
    return False

for c in xrange(1,1001):
    for b in xrange(1,c):
        if c+b>1000:
            break
        for a in xrange(1,b):
            if a+b+c==1000:
                if isPythagoreanTrip(a,b,c):
                    print a*b*c
                    sys.exit()
            elif a+b+c>1000:
                break
                
