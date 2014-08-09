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
def IsTrunctablePrime(n):
    numberlen=len(str(n))
    for i in xrange(1,numberlen):
        if not isprime(n/(10**(numberlen-i))):
            return False
        if not isprime( n%(10**i)):
            return False
    return True

counter=0
summe=0
i=11
Trunctable=[]
while(counter<11):
    i+=6
    if isprime(i):
        if IsTrunctablePrime(i):
            counter+=1
            Trunctable.append(i)
    if isprime(i+2):
        if IsTrunctablePrime(i+2):
            counter+=1
            Trunctable.append(i+2)
print sum(Trunctable)
