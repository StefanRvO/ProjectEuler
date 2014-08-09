#!/usr/bin/python

def isLeapYear(year):
    if year%4==0:
        if year%100:
            if year%400:
                return True
            return False
        return True
    return False

days30=[3,5,8,10]

days31=[0,2,4,6,7,9,11]
monthday=1
weekday=1
year=1900
month=0
sundaycount=0
while(year<2001):
    if monthday==1:
        if weekday==7:
            if year>=1901:
                sundaycount+=1
    monthday+=1
    weekday+=1
    if weekday>7:
        weekday=1
    if month in days30:
        if monthday>30:
            monthday=1
            month+=1
    elif month in days31:
        if monthday>31:
            monthday=1
            month+=1
    else:
        if isLeapYear(year):
            if monthday>29:
                month+=1
                monthday=1
        else:
            if monthday>28:
                month+=1
                monthday=1
    if month>11:
        month=0
        year+=1
print sundaycount
