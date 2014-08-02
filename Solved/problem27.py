#/usr/bin/python
import sys

def isprime(num):
    if num<1:
        return False
    prime=0
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=1
            break
    if prime==0:
        return True
    else:
        return False




a_best=0
b_best=0
maxprimes=0

for b in range(-999,1000):
    for a in range(-999,1000):
        n=0
        while(isprime(n**2+a*n+b)):
            n+=1
        if n>maxprimes:
            print "Found new record.",n,"primes with a:",a,"and b:",b,"product:",a*b
            a_best=a
            b_best=b
            maxprimes=n


