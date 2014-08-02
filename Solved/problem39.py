#!/usr/bin/python

def GetTriangleNumbers(number):
    Triangles=[]
    for i in range(number/2+1):
        for j in range(number/2+1):
            square=(i**2+j**2)**0.5
            if i+j+square==number:
                Triangles.append([i,j,square])
    for i in range(len(Triangles)):
        Triangles[i].sort()
    while(True):
        i=0
        for j in Triangles:
            i+=1
            if Triangles.count(j)>=2:
                Triangles.remove(j)
                i=0
                break
        if i>=len(Triangles):
            break
    return len(Triangles)


maxval=0

for i in range(1000):
    triangles=GetTriangleNumbers(i)
    if triangles>maxval:
        maxval=triangles
        print "New record", i,"With", maxval,"triangles"


