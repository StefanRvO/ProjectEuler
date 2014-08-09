#!/usr/bin/python

def GetNumberLenght(n):
    return len(str(n))


n=0 
counter=0
while(n<50):
    n+=1
    lenght=0
    i=0
    while(lenght<=n):
        i+=1
        lenght=GetNumberLenght(i**n)
        if lenght==n:
            counter+=1
print counter
