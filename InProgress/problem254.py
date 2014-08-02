#!/usr/bin/python

def Factorial(n):
    if n==0:
        return 1
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 6
    if n==4:
        return 24
    if n==5:
        return 120
    if n==6:
        return 720
    if n==7:
        return 5040
    if n==8:
        return 40320
    if n==9:
        return 362880

def f(n):
    return sum(Factorial(int(x)) for x in str(n))
    
def sf(n):
    return sum(int(x) for x in str(f(n)))
    
def g(i):
    if i==45:
        n=9
        while True:
            n+=10
            if sf(n)==i:
                return n
               
    n=0
    while True:
        n+=1
        if sf(n)==i:
            return n
            
def sg(i):
    return sum(int(x) for x in str(g(i)))

summe=0
for i in range(1,100):
    print 45,g(45)
    
