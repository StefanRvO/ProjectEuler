#!/usr/bin/python2
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

primes=0
sidelenght=0
nonprimes=0
ratio=1
currentnum=1
while(ratio>=0.1):
    sidelenght+=2
    for i in range(3):
        currentnum+=sidelenght
        if isprime(currentnum):
            primes+=1
        else:
            nonprimes+=1
    currentnum+=sidelenght
    nonprimes+=1
    ratio=float(primes)/(primes+nonprimes)
print sidelenght-1
