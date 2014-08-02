#!/usr/bin/python
from math import factorial



def calcCompbinations(n,r):
    return (factorial(n))/(factorial(r)*factorial(n-r))



over1million=0
for n in range(1,101):
    for r in range(1,101):
        if r>n:
            break
        combinations=calcCompbinations(n,r)
        if combinations>1000000:
            over1million+=1
print over1million
