#!/usr/bin/python

def IsReversible(n):
    if n[-1]=='0':
        return False
    numlen=len(n)
    carry=False
    for i in xrange(numlen):
        if not carry:
            ciffersum=(int(n[i])+int(n[-(i+1)]))
            if ciffersum%2==0:
                return False
            if ciffersum>=10:
                carry=True
            else:
                carry=False
        else:
            ciffersum=(int(n[i])+int(n[-(i+1)]))+1
            if ciffersum%2==0:
                return False
            if ciffersum>=10:
                carry=True
            else:
                carry=False
    return True

counter=0
for i in xrange(10,10000000):
    stri=str(i)
    if IsReversible(stri):
        counter+=1
    
print counter
