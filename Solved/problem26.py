#!/usr/bin/python
def GetReciprocCycle(p):
    nominator=(10**(p-1))-1
    return nominator/p
def GetReciprocCyclelen(n):
    k=0
    while(True):
        k+=1
        if (10**k)%n==1:
            return k
def isprime(num):
    if num<1:
        return False
    prime=0
    for i in xrange(2,int(num**0.5)+1):
        if num%i==0:
            prime=1
            break
    if prime==0:
        return True
    else:
        return False 
maxlen=0   
maxlennum=0
for i in xrange(1000,0,-1):
    if maxlen>i:
        break
    if isprime(i):
        cyclelen=GetReciprocCyclelen(i)
        if cyclelen>maxlen:
            maxlen=cyclelen
            maxlennum=i
print maxlennum
