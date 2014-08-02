#!/usr/bin/python

def nextdirection(direction):
    if direction=='r':
        return 'u'
    if direction=='u':
        return 'l'
    if direction=='l':
        return 'd'
    else:
        return 'r'

def xystep(x,y,direction):
    if direction=='r':
        return [x,y+1]
    if direction=='u':
        return [x-1,y]
    if direction=='l':
        return [x,y-1]
    else:
        return [x+1,y]


def nextstep(i):
    global x
    global y
    global direction
    global spiralstep
    global Spiral
    global Spiralsize
    global curspiral
    
    xy=xystep(x,y,direction)
    x=xy[0]
    y=xy[1]
    Spiral[x][y]=i
    spiralstep+=1
    if i==2:
        direction='u'
        curspiral=2
        spiralstep=1
    elif i==3:
        direction='l'
        curspiral=3
        spiralstep=1
    elif spiralstep>=curspiral:
        if not i==curspiral**2:
            direction=nextdirection(direction)
            spiralstep=1
        if i==curspiral**2+1:
            curspiral+=1
        
def GetDirectionalSum(Spiral):
    summe=0
    for i in range(len(Spiral)):
        for j in range(len(Spiral)):
            if i==j or i+j+1==len(Spiral):
                summe+=Spiral[i][j]
    return summe
        

def printSpiral(Spiral):
    for i in range(len(Spiral)):
        sprlstr=''
        for j in Spiral[i]:
            sprlstr+='\t'+str(j)
        print sprlstr
Spiralsize=1001 ##Must be an odd number

Spiral=[["." for i in range(Spiralsize)] for i in range(Spiralsize)]


x=Spiralsize/2
y=Spiralsize/2
spiralstep=0
curspiral=1
direction='r'
Spiral[x][y]=1
for i in range(2,Spiralsize*Spiralsize+1):
    nextstep(i)
        
print GetDirectionalSum(Spiral)
