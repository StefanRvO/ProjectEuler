#!/usr/bin/python
import itertools

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


def calcnumber(a,b,c):
    return a**2+b**3+c**4

primelist1=[]
primelist2=[]
primelist3=[]
for i in range(2,int(50000000**0.5)+100):
    if isprime(i):
        if i**2<50000000:
            primelist1.append(i)
        if i**3<50000000:
            primelist2.append(i)
        if i**4<50000000:
            primelist3.append(i)

print "primecalc done"
numbers=[]
for i in range(len(primelist1)):
    a=primelist1[i]
    print i/float(len(primelist1))
    for b in primelist2:
        if (a**2+b**3)>50000000:
            break
        for c in primelist3:
            number=calcnumber(a,b,c)
            if  number<50000000:
                numbers.append(number)
            else:
                break

print len(numbers)
print len(list(set(numbers)))
