#!/usr/bin/python
import sys
def MakeAllPandigitals(numbers):
    Pandigitals=[]
    numberslen=len(numbers)
    times=10**(numberslen-1)
    if numberslen==1:
        return numbers
    for i in xrange(numberslen):
        Pandigitals+=[numbers[i]*times+j for j in MakeAllPandigitals(numbers[:i]+numbers[i+1:])]
    return Pandigitals
def ispandigital(n):
    liststr=list(str(n))
    for digit in xrange(1,len(liststr)+1):
        if not liststr.count(str(digit))==1:
            return False
    return True
def isprime(num):
    if num<1:
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
for i in xrange(9,0,-1):
    for number in sorted(MakeAllPandigitals(range(1,i+1)))[::-1]:
        if isprime(number):
            print number
            sys.exit()
        
