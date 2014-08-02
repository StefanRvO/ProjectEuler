#!/usr/bin/python

def ispandigital(number):
    numberstr=str(number)
    for char in "123456789":
        if not char in numberstr:
            return False
    return True

def concaProd(number,factors):
    numberstr=""
    for factor in factors:
        numberstr+=str(number*factor)
    return numberstr




i=0
while(True):
    i+=1
    n=9/len(str(i))
    if n==1:
        break
    if ispandigital(concaProd(i,range(1,n+1))) and len(concaProd(i,range(1,n+1)))==9:
        print concaProd(i,range(1,n+1)),"\t",i,"\t",n
