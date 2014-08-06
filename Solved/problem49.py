#!/usr/bin/python

def MakeAllPermutations(numbers):
    permutations=[]
    numberslen=len(numbers)
    times=10**(numberslen-1)
    if numberslen==1:
        return numbers
    for i in xrange(numberslen):
        permutations+=[numbers[i]*times+j for j in MakeAllPermutations(numbers[:i]+numbers[i+1:])]
    return permutations
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
def getSequenceNumbers(primes):
    for i in xrange(len(primes)-2):
        for j in xrange(i,len(primes)-1):
            for k in xrange(j,len(primes)):
                if abs(primes[i]-primes[j])==abs(primes[j]-primes[k]) and abs(primes[j]-primes[k])!=0:
                    return [primes[i],primes[j],primes[k]]
    return []
tested=[]           
for i in xrange(1000,10000):
    istr=sorted(list(str(i)))
    if istr in tested:
        continue
    tested.append(istr)
    permutations=list(set(MakeAllPermutations([int(x) for x in istr])))
    primepermutations=[prime for prime in permutations if isprime(prime)]
    numbers= sorted(getSequenceNumbers(primepermutations))
    for number in numbers:
        if len(str(number))!=4:
            numbers.remove(number)
    if len(numbers)==3:
        print numbers, ''.join(str(number) for number in numbers)
