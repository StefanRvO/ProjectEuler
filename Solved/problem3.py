#!/usr/bin/python
def isprime(num):
    if num<=1:
        return False
    prime=0
    if num==2 or num==3:
        return True
    if num%2==0:
        return False
    for i in xrange(5,int(num**0.5)+1,2):
        if num%i==0:
            prime=1
            break
    if prime==0:
        return True
    else:
        return False
        
def GetPrimeFactors(n):
    factors=[]
    for i in xrange(2,int(n**0.5)+1):
        if n%i==0:
            factors.append(i)
    primes=[]
    for i in factors:
        if isprime(i):
            primes.append(i)
            
    return primes

print max(GetPrimeFactors(600851475143))
