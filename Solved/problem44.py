#!/usr/bin/python
import sys
def Pentainv(n):
    return 1./6+1./6*((1+24*n)**0.5)
def IsPentagonNumber(n):
    inv=Pentainv(n)
    if int(round(inv,5))== round(inv,5):
        return True
    return False
def PentagonNumber(n):
    return n*(3*n-1)/2

i=0

#print(IsPentagonNumber(146))
#sys.exit()
mindiff=99999999999999999
while(True):
    i+=1
    pentagon1=PentagonNumber(i)
    for j in xrange(1,i):
        pentagon2=PentagonNumber(j)
        if IsPentagonNumber(pentagon1-pentagon2) and IsPentagonNumber(pentagon1+pentagon2):
            if mindiff>pentagon1-pentagon2:
                mindiff=pentagon1-pentagon2
                print "Found new record!",pentagon1-pentagon2,"by",pentagon1,"and",pentagon2,"created by",i,"and",j
                sys.exit()
                

