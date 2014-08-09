#!/usr/bin/python

def isDBP(n): #DBP=Double-Base palindrome
    numstr_10=str(n)
    numstr_2=bin(n)[2:]
    return isPalindrome(numstr_10) and isPalindrome(numstr_2)

def isPalindrome(numstr):
    if numstr[-1]=="0":
        return False
    for i in xrange(len(numstr)>>1):
        if not numstr[i]==numstr[-(i+1)]:
            return False
    return True
    
summe=0
for i in xrange(1000000):
    if isDBP(i):
       summe+=i
print summe
