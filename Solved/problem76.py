#!/usr/bin/python

def p(n):
    global parts
    if n<0:
        return 0
    if n<=1:
        return 1
    if len(parts)>n:
    
        return parts[n]
    summe=0
    for k in xrange(1,n+1):
        part1=n-k*(3*k-1)/2
        part2=n-k*(3*k+1)/2
        if part1<0:
            break
        if k%2==0:
            if part1>=0:
                summe-=parts[part1]
            if part2>=0:
                summe-=parts[part2]
        else:
            if part1>=0:
                summe+=parts[part1]
            if part2>=0:
                summe+=parts[part2]
    return summe

target=100
i=0
parts=[]
for i in range(target):
    j=p(i)
    parts.append(j)
    i+=1
print p(target)-1

