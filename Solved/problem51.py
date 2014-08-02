#/usr/bin/python
import sys
from itertools import combinations

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


def GetPrimeCount(numberList): #Return how many primenumbers the list contian
    primes=0
    for num in numberList:
        if isprime(num):
            primes+=1
    return primes

def DoThisReplacement(number,places):
    numlist=[]    
    strnumber=str(number)
    numlen=len(strnumber)
    for i in range(10):
        for l in places:
            strnumber=strnumber[:l]+str(i)+strnumber[l+1:]
        numlist.append(int(strnumber))
        strnumber=str(number)
    for i in range(len(numlist)):
        if not (len(str(numlist[i]))==numlen):
            numlist.remove(numlist[i])
            break
    return list(set(numlist))

def GenerateReplacements(number):
    global maxprimes
    global BestCase
    numlenght=len(str(number))
    replacelist=range(numlenght)
    for i in range(1,numlenght):
        Replacements=combinations(replacelist,i)
        for case in Replacements:
            group=DoThisReplacement(number,case)
            primesInGroup=GetPrimeCount(group)
            if primesInGroup>maxprimes:
                print "New Record",number,"with",primesInGroup,"primes in group", sorted(group)
                maxprimes=primesInGroup
                BestCase=number

    

global BestCase
BestCase=0
global maxprimes
maxprimes=0

for i in range(1,10000000,2):
    if isprime(i):
        GenerateReplacements(i)

