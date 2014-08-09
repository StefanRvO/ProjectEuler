#!/usr/bin/python
loopnumbers=[169,363601,1454,871,45361,872,45362]
def DigFac(n):
    prod=1
    for i in xrange(2,n+1):
        prod*=i
    return prod
   
   
def FacDigitSum(n):
    numstr=str(n)
    summe=0
    for char in numstr:
        if char=='0':
            summe+=1
        elif char=='1':
            summe+= 1
        elif char=='2':
            summe+=  2
        elif char=='3':
            summe+=  6
        elif char=='4':
            summe+=  24
        elif char=='5':
            summe+= 120
        elif char=='6':
            summe+=720
        elif char=='7':
            summe+=5040
        elif char=='8':
            summe+=40320
        elif char=='9':
            summe+=362880
    return summe
    
def GetChainLenght_nR(n):
    loopnumcounter=0
    counter=0
    last=0
    while True:
        counter+=1
        if n in loopnumbers:
            loopnumcounter+=1
            if loopnumcounter==2:
                counter+=1
                break
        last=n
        n=FacDigitSum(n)
        if n==last:
            break
    return counter

counter=0
for i in xrange(1000000):
    if GetChainLenght_nR(i)==60:
        counter+=1
print counter
