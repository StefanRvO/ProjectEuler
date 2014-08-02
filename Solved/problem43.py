#!/usr/bin/python
from itertools import permutations
numbers=['0','1','2','3','4','5','6','7','8','9']

def iswonder(n):
    if not int(n[1:4])%2==0:
        return False
    if not int(n[2:5])%3==0:
        return False
    if not int(n[3:6])%5==0:
        return False
    if not int(n[4:7])%7==0:
        return False
    if not int(n[5:8])%11==0:
        return False
    if not int(n[6:9])%13==0:
        return False
    if not int(n[7:10])%17==0:
        return False
    return True


permutations=list(permutations(numbers,10))
newpermutations=[]
for number in permutations:
    if not number[0]=='0':
        numberstr=''
        for char in number:
            numberstr+=char
        newpermutations.append(numberstr)

summe=0
for number in newpermutations:
    if iswonder(number):
        summe+=int(number)
print summe
