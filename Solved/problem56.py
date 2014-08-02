#!/usr/bin/python

def GetDigitSum(number):
    numberstr=str(number)
    digitsum=0
    for i in numberstr:
        digitsum+=int(i)
    return digitsum


maxsum=0
for a in range(100):
    for b in range(100):
        digitsum=GetDigitSum(a**b)
        if digitsum>maxsum:
            print "New record a:",a,"b:",b,"digitsum:",digitsum
            maxsum=digitsum
        
