#!/usr/bin/python
import sys

def IsGridValid():
    for i in xrange(4):
        RowSum=Grid[i*4]+Grid[i*4+1]+Grid[i*4+2]+Grid[i*4+3]
        if not RowSum==12:
            return False
        CollumnSum=Grid[i]+Grid[i+4]+Grid[i+8]+Grid[i+12]
        if not CollumnSum==12:
            return False
    return True
         
def Possibilities(n):
    Possibilities=[]
    for i in range(10):
        for j in range(10):
            for k in range(10):
                for l in range(10):
                    if i+j+k+l==n:
                        Possibilities.append([i,j,k,l])
    return Possibilities

def nextindexd(place,index,lenpos,goal):
    while(possibilities[index][place]<=goal and index<lenpos-1):
        index+=1
        
    return index+1
def nextindexu(place,index,lenpos):
    initval=possibilities[index][place]
    while(possibilities[index][place]>=initval and index<lenpos-1):
        index+=1
    return index+1
counter=0
while True:
    i=12
    possibilities=Possibilities(i)
    lenpos=len(possibilities)
    j=0
    while j<lenpos:
        print j
        if i<9:
            if possibilities[j][0]>i:
                break
            if possibilities[j][1]>i:
                j=nextindexu(1,j,lenpos)
                continue
            if possibilities[j][2]>i:
                j=nextindexu(2,j,lenpos)
                continue
            if possibilities[j][3]>i:
                j=nextindexu(3,j,lenpos)
                continue
        elif i>27:
            if possibilities[j][0]<36-i:
                j=nextindexd(0,j,lenpos,36-i)
                continue
            if possibilities[j][1]<36-i:
                j=nextindexd(1,j,lenpos,36-i)
                continue
            if possibilities[j][2]<36-i:
                j=nextindexd(2,j,lenpos,36-i)
                continue
            if possibilities[j][3]>36-i:
                j=nextindexd(3,j,lenpos,36-i)
                continue        
        k=0
        while k<lenpos:
            if i<18:
                if possibilities[j][0]+possibilities[k][0]>i:
                    break
                if possibilities[j][1]+possibilities[k][1]>i:
                    k=nextindexu(1,k,lenpos)
                    continue
                if possibilities[j][2]+possibilities[k][2]>i:
                    k=nextindexu(2,k,lenpos)
                    continue
                if possibilities[j][3]+possibilities[k][3]>i:
                    k=nextindexu(3,k,lenpos)
                    continue
                if possibilities[j][0]+possibilities[k][1]>i:
                    k=nextindexu(1,k,lenpos)
                    continue
                if possibilities[j][3]+possibilities[k][2]>i:
                    k=nextindexu(2,k,lenpos)
                    continue
            elif i>18:
                if possibilities[j][0]+possibilities[k][0]<36-i:
                    k=nextindexd(0,k,lenpos,36-i-possibilities[j][0])
                    continue
                if possibilities[j][1]+possibilities[k][1]<36-i:
                    k=nextindexd(1,k,lenpos,36-i-possibilities[j][1])
                    continue
                if possibilities[j][2]+possibilities[k][2]<36-i:
                    k=nextindexd(2,k,lenpos,36-i-possibilities[j][2])
                    continue
                if possibilities[j][3]+possibilities[k][3]<36-i:
                    k=nextindexd(3,k,lenpos,36-i-possibilities[j][3])
                    continue
                if possibilities[j][0]+possibilities[k][1]>36-i:
                    k=nextindexd(1,k,lenpos,36-i-possibilities[j][0])
                    continue
                if possibilities[j][3]+possibilities[k][2]>36-i:
                    k=nextindexd(2,k,lenpos,36-i-possibilities[j][3])
                    continue
            l=0
            while l<lenpos:
                if i<27:
                    if possibilities[j][0]+possibilities[k][0]+possibilities[l][0]>i:
                        break
                    if possibilities[j][1]+possibilities[k][1]+possibilities[l][1]>i:
                        l=nextindexu(1,l,lenpos)
                        continue
                    if possibilities[j][2]+possibilities[k][2]+possibilities[l][2]>i:
                        l=nextindexu(2,l,lenpos)
                        continue
                    if possibilities[j][3]+possibilities[k][3]+possibilities[l][3]>i:
                        l=nextindexu(3,l,lenpos)
                        continue
                    if possibilities[j][0]+possibilities[k][1]+possibilities[l][2]>i:
                        l=nextindexu(2,l,lenpos)
                        continue
                    if possibilities[j][3]+possibilities[k][2]+possibilities[l][1]>i:
                        l=nextindexu(1,l,lenpos)
                        continue
                if i>9:
                    if possibilities[j][0]+possibilities[k][0]+possibilities[l][0]<36-i:
                        l=nextindexd(0,l,lenpos,36-i-(possibilities[j][0]+possibilities[k][0]))
                        continue
                    if possibilities[j][1]+possibilities[k][1]+possibilities[l][1]<36-i:
                        l=nextindexd(1,l,lenpos,36-i-(possibilities[j][1]+possibilities[k][1]))
                        continue
                    if possibilities[j][2]+possibilities[k][2]+possibilities[l][2]<36-i:
                        l=nextindexd(2,l,lenpos,36-i-(possibilities[j][2]+possibilities[k][2]))
                        continue
                    if possibilities[j][3]+possibilities[k][3]+possibilities[l][3]<36-i:
                        l=nextindexd(3,l,lenpos,36-i-(possibilities[j][3]+possibilities[k][3]))
                        continue
                    if possibilities[j][0]+possibilities[k][1]+possibilities[l][2]<36-i:
                        l=nextindexd(2,l,lenpos,36-i-(possibilities[j][0]+possibilities[k][1]))
                        continue
                    if possibilities[j][3]+possibilities[k][2]+possibilities[l][1]<36-i:
                        l=nextindexd(1,l,lenpos,36-i-(possibilities[j][3]+possibilities[k][2]))
                        continue
                m=0
                while m<lenpos:
                    if possibilities[j][0]+possibilities[k][0]+possibilities[l][0]+possibilities[m][0]>i:
                        break
                    if possibilities[j][3]+possibilities[k][2]+possibilities[l][1]+possibilities[m][0]>i:
                        break
                    if possibilities[j][1]+possibilities[k][1]+possibilities[l][1]++possibilities[m][1]>i:
                        m=nextindexu(1,m,lenpos)
                        continue
                    if possibilities[j][2]+possibilities[k][2]+possibilities[l][2]+possibilities[m][2]>i:
                        m=nextindexu(2,m,lenpos)
                        continue
                    if possibilities[j][3]+possibilities[k][3]+possibilities[l][3]++possibilities[m][3]>i:
                        m=nextindexu(3,m,lenpos)
                        continue
                    if possibilities[j][0]+possibilities[k][1]+possibilities[l][2]++possibilities[m][3]>i:
                        m=nextindexu(3,m,lenpos)
                        continue
                    if  possibilities[j][0]+possibilities[k][0]+possibilities[l][0]+possibilities[m][0]<36-i:
                        m=nextindexd(0,m,lenpos,36-i-(possibilities[j][0]+possibilities[k][0]+possibilities[l][0]))
                        continue
                    if possibilities[j][1]+possibilities[k][1]+possibilities[l][1]++possibilities[m][1]<36-i:
                        m=nextindexd(1,m,lenpos,36-i-(possibilities[j][1]+possibilities[k][1]+possibilities[l][1]))
                        continue
                    if possibilities[j][2]+possibilities[k][2]+possibilities[l][2]+possibilities[m][2]<36-i:
                        m=nextindexd(2,m,lenpos,36-i-(possibilities[j][2]+possibilities[k][2]+possibilities[l][2]))
                        continue
                    if possibilities[j][3]+possibilities[k][3]+possibilities[l][3]++possibilities[m][3]<36-i:
                        m=nextindexd(3,m,lenpos,36-i-(possibilities[j][3]+possibilities[k][3]+possibilities[l][3]))
                        continue
                    if possibilities[j][0]+possibilities[k][1]+possibilities[l][2]++possibilities[m][3]<36-i:
                        m=nextindexd(3,m,lenpos,36-i-(possibilities[j][0]+possibilities[k][1]+possibilities[l][2]))
                        continue
                    if possibilities[j][3]+possibilities[k][2]+possibilities[l][1]+possibilities[m][0]<36-i:
                        m=nextindexd(0,m,lenpos,36-i-(possibilities[j][3]+possibilities[k][2]+possibilities[l][1]))
                        continue
                    counter+=1
                    m+=1
                l+=1
            k+=1
        j+=1
    print counter
