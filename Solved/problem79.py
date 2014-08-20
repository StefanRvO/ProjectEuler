#!/usr/bin/python
import sys

def loadkeys():
    file=open("keylog.txt")
    keys=file.readlines()
    for i in xrange(len(keys)):
        keys[i]=keys[i][:-1]
    return keys
    
def ComesJAfter(n,keys,dontcount):
    AfterList=[]
    for key in keys:
        if n in key:
            if not key[-1]==n:
                AfterList.append(key[key.index(n)+1])
                if AfterList[-1] in dontcount:
                    AfterList.remove(AfterList[-1])

    return sorted(list(set(AfterList)))
def ComesJBefore(n,keys,dontcount):
    BeforeList=[]
    for key in keys:
        if n in key:
            if not key[0]==n:
                BeforeList.append(key[key.index(n)-1])
                if BeforeList[-1] in dontcount:
                    BeforeList.remove(BeforeList[-1])

    return sorted(list(set(BeforeList)))
def ValidNumbers(keys):
    numbers=[]
    for key in keys:
        for i in key:
            numbers.append(i)
    return sorted(list(set(numbers)))
    
keys= sorted(list(set(loadkeys())))
numbers=ValidNumbers(keys)
#sys.exit()
string=""
donenumbers=[]
while(len(numbers)!=0):
    for n in numbers:
        if len(ComesJBefore(n,keys,donenumbers))==0:
            string+=n
            numbers.remove(n)
            donenumbers.append(n)
            break
    print string
    numbers=ComesJAfter(string[-1],keys,donenumbers)

