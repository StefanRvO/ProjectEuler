#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import time

factorirallist=[1]
def factorial(n):
    global factorirallist
    if n==1 or n==0:
        return 1    
    summe=1
    if len(factorirallist)>n:
        return factorirallist[n]
    for i in range(1,n+1):
        if len(factorirallist)>i:
            continue
        if len(factorirallist)==i:
            summe=factorirallist[-1]
        summe*=i
        if len(factorirallist)==i:
            factorirallist.append(summe)
    return summe

def GetFactorialDigitSum(n):
    summe=0
    for digit in str(n):
        summe+=factorial(int(digit))
    return summe

x=[]
y=[]

for i in range(1,2000000):
    if i==GetFactorialDigitSum(i):
        print i
