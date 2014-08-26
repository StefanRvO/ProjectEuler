import gmpy2
import itertools
import math
import sys
primes=[]




def numcat(a,b):
    return int(str(a)+str(b))
    #return int(math.pow(10,(int(math.log(b,10)) + 1)) * a + b)
    




j=2
while (j<27000):
    j=gmpy2.next_prime(j)
    primes.append(j)
    
primefits=[]
    
for i in range(len(primes)):
    primefits.append([primes[l] for l in range(i+1,len(primes)) if (gmpy2.is_prime(numcat(primes[i],primes[l])) and gmpy2.is_prime(numcat(primes[l],primes[i])))  ])


hits=[]    
for fit1 in primefits:
    if not (len(fit1)):
        continue
    for fit2 in fit1:
        index1=primes.index(fit2)
        if not len(primefits[index1]):
            continue
        for fit3 in (primefits[index1]):
            if not fit3 in fit1:
                continue
            index2=primes.index(fit3)
            if not len(primefits[index2]):
                continue
            for fit4 in (primefits[index2]):
                if not ((fit4 in primefits[index1]) and (fit4 in fit1)):
                    continue
                index3=primes.index(fit4)
                if not len(primefits[index3]):
                    continue
                for fit5 in (primefits[index3]):
                    if not ((fit5 in fit1) and (fit5 in primefits[index1]) and (fit5 in primefits[index2])):
                        continue
                    hits.append([fit5,fit4,fit3,fit2,primes[primefits.index(fit1)]])

print min([sum(j) for j in hits])

