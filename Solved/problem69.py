#!/usr/bin/python2
import sys
def getPrimeDivisors(number):    #returns a list of divisors
    divisors=[]
    if number%2==0:
        divisors.append(2)
    if number%3==0:
        divisors.append(3)
    
    for i in xrange(5,int(number**0.5)+1,2):
        if number%i==0:
            if isprime(i):
                divisors.append(i)
    return divisors
    
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

def GetPhi1(n):
    y = n
    for i in range(2,n+1):
        if isprime(i) and n % i == 0:
            y *= 1 - 1.0/i
    return int(y)
def GetPhi2(n):
    prod=n
    for divisor in getPrimeDivisors(n):
        prod*=(1-1./divisor)
    return prod            


record=0
for i in xrange(2,1000001):
    testrecord=float(i)/GetPhi2(i)
    if testrecord>record:
        print i,testrecord
        record=testrecord
