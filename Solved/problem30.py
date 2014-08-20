#!/usr/bin/python


def FindPowerSum(number,power):
    strnumber=str(number)
    summe=0
    for digit in strnumber:
        summe+=int(digit)**power
    return summe


summe=0
for testing in range(10,9**6*7):
    if testing==FindPowerSum(testing,5):
        summe+=testing
        print testing

print "\n\n\n",summe
