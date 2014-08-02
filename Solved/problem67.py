#!/usr/bin/python

def loadTriangle():
    file=open('bigtriangle.txt')
    triangle=file.read()
    triangle=triangle.split('\n')[:-1]
    for i in range(len(triangle)):
        triangle[i]=triangle[i].split(' ')
        for j in range(len(triangle[i])):
            triangle[i][j]=int(triangle[i][j])
    return triangle    

triangle=loadTriangle()
emptytriangle=[]
for i in range(len(triangle)):
    emptytriangle.append([])
    for j in range(len(triangle[i])):
        emptytriangle[i].append('')
for i in range(len(triangle)-1,-1,-1):
    for j in range(len(triangle[i])):
        if i==len(triangle)-1:
            emptytriangle[i][j]=triangle[i][j]
        else:
            emptytriangle[i][j]=triangle[i][j]+max([emptytriangle[i+1][j],emptytriangle[i+1][j+1]])
print emptytriangle[0][0]

