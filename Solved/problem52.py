#!/usr/bin/python


def CheckSameDigits(num1,num2): #check if the two numbers contain the same digits
    if (sorted(list(str(num1)))==sorted(list(str(num2)))):
        return True
    else:
        return False

def GetPermutations(number): #Return how many times a number can be multiplied by an integer and still contain the same digits, eg 1x,2x,3x
    i=2
    while(CheckSameDigits(number,number*i)):
        i+=i
    return i-2



maxPermutations=0
for i in range(1,10000000):
    CurPer=GetPermutations(i)
    if CurPer>maxPermutations:
        print "New Record",i,"with",CurPer,"Permutations."
        maxPermutations=CurPer


