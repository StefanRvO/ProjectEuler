#!/usr/bin/python


def isPrime( n):
    if (n<=1):
        return False
    if (n==2):
        return True
    if (n%2==0):
        return False;
    for i in xrange(3,int(n**0.5)+1,2): 
        if (n%i==0):
            return False
    return True


def GetRemainder(prime, power):
    upper=pow(prime-1,power,prime**2)+pow(prime+1,power,prime**2)
    return upper%(prime**2)
    
    
pcounter=1
for i in xrange(3,10000000,2):
    if isPrime(i):
        pcounter+=1
        if GetRemainder(i,pcounter)>10**10:
            print pcounter
            break
            
            
