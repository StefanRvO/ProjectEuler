#!/usr/bin/python

def isprime(num):
    if num<=1:
        return False
    prime=0
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            prime=1
            break
    if prime==0:
        return True
    else:
        return False
def shiftright(string):
    return  string[-1]+string[:-1]

def isCurcularPrime(num):
    if not isprime(num):
        return False
    numstr=str(num)
    for i in range(len(numstr)-1):
        numstr=shiftright(numstr)
        if not isprime(int(numstr)):
            return False
    return True

counter=1
for i in range(3,1000000,2):
    if isCurcularPrime(i):
        counter+=1
print counter
            
