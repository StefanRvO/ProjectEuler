#!/usr/bin/python

def getDivisors(number):    #returns a list of divisors
    divisors=[1]
    if number%2!=0:
        for i in range(3,int(number**0.5)+1,2):
            if number%i==0:
                divisors.append(i)
                divisors.append(number/i)
    else:
        for i in range(2,int(number**0.5)+1):
            if number%i==0:
                divisors.append(i)
                divisors.append(number/i)
    return list(set(divisors))
    
def isAbundant(n):
    if sum(getDivisors(n))>n:
        return True
    return False

Abundantnumbers=[]
     
summe=0       
for i in range(1,28123):
    if isAbundant(i):
        Abundantnumbers.append(i)
sumAbundant=[]

for i in Abundantnumbers:
    for j in Abundantnumbers:
        if j+i>28123:
            break
        sumAbundant.append(i+j)
sumAbundant=list(set(sumAbundant))
summe=0     
for i in range(28123):
    if not i in sumAbundant:
        summe+=i
print summe 

