#!/usr/bin/python
import math

def loadnumbers():
    file=open("base_exp.txt")
    numbers=file.readlines()
    newnumbers=[]
    for num in numbers:
        numbers[numbers.index(num)]=[int(x) for x in num[:-1].split(',')]
        
    return numbers

def comparenumbers(n1,n2): #n1[0] is base n1[1] is exponent
    #convert numbers to log_e form
    logform1=n1[1]*math.log(n1[0])
    logform2=n2[1]*math.log(n2[0])
    return logform1>logform2
    
    
Numbers=loadnumbers()
while len(Numbers)>1:
    i=0
    while i<len(Numbers)-1:
        if comparenumbers(Numbers[i],Numbers[i+1]):
            Numbers.remove(Numbers[i+1])
        else:
            Numbers.remove(Numbers[i])
print loadnumbers().index(Numbers[0])+1
