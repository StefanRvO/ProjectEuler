#!/usr/bin/python

def loadNumbers():
    return open("roman.txt").read().splitlines()
    



def FromRomandToDecimal(RomanString):
    NumberList=[]
    for char in RomanString:
        if char=='M':
            NumberList.append(1000)
        elif char=='D':
            NumberList.append(500)
        elif char=='C':
            NumberList.append(100)
        elif char=='L':
            NumberList.append(50)
        elif char=='X':
            NumberList.append(10)
        elif char=='V':
            NumberList.append(5)
        elif char=='I':
            NumberList.append(1)
    return NumberList
def MinimizeRoman(RomanString):
    DecimalList=FromRomandToDecimal(RomanString)
    Number=CalcNumber(DecimalList)
    return FromDecimalToRoman(Number)
    
def CalcNumber(NumberList):
    if len(NumberList)==1:
        return NumberList[0]
    if NumberList[0]>=NumberList[1]:
        return NumberList[0]+CalcNumber(NumberList[1:])
    else:
        return CalcNumber(NumberList[1:])-NumberList[0]
def FromDecimalToRoman(number):
    if number==0:
        return ''
    if number>=1000:
        return 'M'+FromDecimalToRoman(number-1000)
    if number>=900:
        return 'CM'+FromDecimalToRoman(number-900)
    if number>=500:
        return 'D'+FromDecimalToRoman(number-500)
    if number>=400:
        return 'CD'+FromDecimalToRoman(number-400)
    if number>=100:
        return 'C'+FromDecimalToRoman(number-100)
    if number>=90:
        return 'XC'+FromDecimalToRoman(number-90)
    if number>=50:
        return 'L'+FromDecimalToRoman(number-50)
    if number>=40:
        return 'XL'+FromDecimalToRoman(number-40)
    if number>=10:
        return 'X'+FromDecimalToRoman(number-10)
    if number>=9:
        return 'IX'+FromDecimalToRoman(number-9)
    if number>=5:
        return 'V'+FromDecimalToRoman(number-5)
    if number>=4:
        return 'IV'+FromDecimalToRoman(number-4)
    return 'I'+FromDecimalToRoman(number-1)
        
        
Numbers=loadNumbers()

lencounterU=0
lencounterM=0
for Number in Numbers:
    lencounterU+=len(Number)
    lencounterM+=len(MinimizeRoman(Number))
print lencounterU-lencounterM

        
