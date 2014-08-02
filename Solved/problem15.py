#/usr/bin/python
import sys
n=int(sys.argv[1])

def getpathlenght(posx,posy):
    global patharray

    if posx==0 or posy==0:
        patharray[posx][posy]=1 #There is only one path to these
    if patharray[posx][posy]=='':
        patharray[posx][posy]=getpathlenght(posx-1,posy)+getpathlenght(posx,posy-1)
    
    #print posx,posy
    return patharray[posx][posy]


patharray = [['']*(n+1) for _ in range(n+1)] 

print getpathlenght(n,n)


