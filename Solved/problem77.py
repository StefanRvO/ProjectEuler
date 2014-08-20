#!/usr/bin/python
primes=[]
ways=[]


def isprime(num):
    if num<=1:
        return False
    prime=0
    if num==2:
        return True
    if num%2==0:
        return False
    for i in xrange(3,int(num**0.5)+1,2):
        if num%i==0:
            prime=1
            break
    if prime==0:
        return True
    else:
        return False


def waysToSum(n):
    global primes
    global ways
    if len(ways)>n:
        if ways[n]!=0:
            return ways[n]
    i=0
    curways=0
    while(primes[i]<=n):
        j=primes[i]
        while(j<=n):
            ways[j]+=ways[(j-primes[i])]
            j+=1
        i+=1
    return ways[n-1]


primes=[x for x in range(1000) if isprime(x)]
i=1
while True:
    i+=1
    ways=[0]*(i+1)
    ways[0]=1
    sumways=0
    prevsumways=1
    while(sumways!=prevsumways):
        prevsumways=sumways
        sumways=waysToSum(i)
    print i,sumways
    if sumways>5000:
        break
