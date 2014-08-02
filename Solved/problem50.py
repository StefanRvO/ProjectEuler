#!/usr/bin/python

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

limit=1000000
primes=[2]
def findnextitem(n,liste):
    return min(xrange(len(liste)), key=lambda i: abs(liste[i]-n))

for i in xrange(3,limit,2):
    if isprime(i):
        primes.append(i)

maxlenght=1
for prime in primes[-1000:]:
    if maxlenght>10:
        searchsize=findnextitem(prime/200.,primes)
    else:
        searchsize=findnextitem(prime/2.,primes)
    for i in xrange(searchsize):
        for j in xrange(searchsize-i):
            primesum=sum(primes[i:j+i])
            if prime==primesum:
                if maxlenght<j:
                    maxlenght=j
                    print "New record",prime,"with",maxlenght,"primes."
            elif prime<primesum:
                break
                
