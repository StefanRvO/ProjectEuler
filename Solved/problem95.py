#!/usr/bin/python
tested=[]
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

def getAmicableChain(number,recur=0):
    global tested
    if number not in tested:
        tested.append(number)
    elif recur==0:
        return False
    startnumber=number
    chain=[]
    while(number not in chain):
        if number>1000000:
            return False
        chain.append(number)
        if number==1:
            return False
        number=sum(getDivisors(number))
        if number not in chain:
            if number not in tested:
                tested.append(number)
            elif recur==0:
                return False
    if not recur:
        return getAmicableChain(chain[-1],1)
    else:
        return chain
maxlenght=0
for i in range(5,1000000):
    if i%10000==0:
        print i/1000000.
    chain=getAmicableChain(i)
    if not chain==False:
        chainlen=len(chain)
        if chainlen>maxlenght:
            maxlenght=chainlen
            print maxlenght,"\t\t",min(chain)
    #else:
        #print "excedded 10^6"
