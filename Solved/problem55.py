#!/usr/bin/python

def isPalindrome(number): #Checks if a number is a palindrome
    strnumber=str(number)
    palindrome=True
    for i in range(len(strnumber)/2+1):
        if not strnumber[-(i+1)]==strnumber[i]:
            return False
    return True
           



def isLychrel(number):
    for i in range(50):
        revnumber=int(str(number)[::-1])
        number=revnumber+number
        if isPalindrome(number):
            return False
    return True

lychrels=0


for i in range(10000):
    if isLychrel(i):
        lychrels+=1
print lychrels
        

