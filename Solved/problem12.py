#!/usr/bin/python


def getDivisors(number):    #returns a list of divisors
    divisors=[]
    if number%2==0:
        for i in range(1,int(number**0.5)+1):
            if number%i==0:
                divisors.append(i)
                divisors.append(number/i)
        return divisors
    else:
        return [1] #Hack all odd numbers will be wrong
        

def MakeTriangleNumber(i):
    return sum(range(1,i+1))

i=1
maxdivisors=0
while(True):
    TriangleNumber=MakeTriangleNumber(i)
    divisors=getDivisors(TriangleNumber)
    if len(divisors)>maxdivisors:
        maxdivisors=len(divisors)
        print "New record",str(i)+"th triangle number",TriangleNumber,"with",maxdivisors,"divisors!"
    i+=1
