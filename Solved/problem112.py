#!/usr/bin/python
def isBouncy(n):
    numberstr=str(n)
    sortednumberstr=''.join(sorted(numberstr))
    if sortednumberstr[::-1]==numberstr: #isdecreasing?
        return False
    if sortednumberstr==numberstr: #isincreasing?
        return False
    return True

#def isDecreasing(numberstr,sortednumberstr):
#    if sortednumberstr[::-1]==numberstr:
#        return True
#    return False
#
#def isIncreasing(numberstr,sortednumberstr):
#    if sortednumberstr==numberstr:
#        return True
#    return False


Bouncy=0.
nonBouncy=0
i=0
ratio=0
while(ratio<0.99):
    i+=1
    if(isBouncy(i)):
        Bouncy+=1
        ratio=Bouncy/(Bouncy+nonBouncy)
        continue
    nonBouncy+=1
print i
