#!/usr/bin/python
import sys
def getPrimefactors(number):    #returns a list of divisors
    divisors=[]
    if number%2!=0:
        for i in xrange(3,int(number**0.5)+1,2):
            if number%i==0:
                divisors.append(i)
                divisors.append(number/i)
    else:
        for i in xrange(2,int(number**0.5)+1):
            if number%i==0:
                divisors.append(i)
                divisors.append(number/i)
    return [x for x in list(set(divisors)) if isprime(x)]
def isprime(num):
    if num<=1:
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

i=0
while(True):
    i+=1
    if len(getPrimefactors(i))==4:
        if len(getPrimefactors(i+1))==4:
            if len(getPrimefactors(i+2))==4:
                if len(getPrimefactors(i+3))==4:
                    print i
                    sys.exit()
                    
