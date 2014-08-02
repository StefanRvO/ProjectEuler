#!/usr/bin/python
import math
layer=5000
factorirallist=[1]
def factorial(n):
    global factorirallist
    if n==1 or n==0:
        return 1    
    summe=1
    if len(factorirallist)>n:
        return factorirallist[n]
    for i in range(1,n+1):
        if len(factorirallist)>i:
            continue
        if len(factorirallist)==i:
            summe=factorirallist[-1]
        summe*=i
        if len(factorirallist)==i:
            factorirallist.append(summe)
    return summe


def calcplacement(facn,fack,n,k):
    return (facn/(fack*factorial(n-k)))

def Findlayer(n):
    facn=factorial(n)
    layerlist=[]
    progress=0
    progressstep=0.1
    nextprogress=progress+progressstep
    for k in range(n+1):
        if k<5:
            fack=factorial(k)
        else:
            fack*=k
        layerlist.append(calcplacement(facn,fack,n,k))
        progress=k/float(n+1)
        if progress>=nextprogress:
            nextprogress=progress+progressstep
            print str(progress*100)+"% done with this layer!"
    return layerlist

calclayer= Findlayer(layer)
