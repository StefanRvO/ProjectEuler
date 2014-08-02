#/usr/bin/python

import sys,fractions
l=int(sys.argv[1])

i=0
for d in range(1,l+1):
    for n in range(1,l+1):
        #if not n<d:
        #    break
        if (d%2==0 and n%2==0):
            continue
        if (d%3==0 and n%3==0):
            continue
        if (d%5==0 and n%5==0):
            continue
        if (d%7==0 and n%7==0):
            continue
        if (d%11==0 and n%11==0):
            continue
        if (d%13==0 and n%13==0):
            continue
        if (d%17==0 and n%17==0):
            continue
        if (d%19==0 and n%19==0):
            continue
        if (d%23==0 and n%23==0):
            continue
        if (d%27==0 and n%27==0):
            continue
        if (d%29==0 and n%29==0):
            continue
        if (d%31==0 and n%31==0):
            continue
        if not fractions.gcd(n,d)==1:
            continue
        i+=1
    if d%10==0:
        print n
        #print str(n)+"/"+str(d)

print i
