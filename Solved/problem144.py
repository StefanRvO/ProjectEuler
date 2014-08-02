#!/usr/bin/python
import math
import pygame
from pygame.locals import *
import time
#Elipse formula=4x^2+y^2=100
#=(x^2/5^2)+(y^2/10^2)=1

SCREENSIZE = (600, 600)
FONTUSED = "Times New Roman"
BACKGROUNDCOLOR = (255, 255, 255)
ELIPSECOLOR=(0,0,0)
LINECOLOR=(0,0,255)
def MultiplyVektor(vec,mul):
    return [x*mul for x in vec]
    
def dotproduct(vec1,vec2):
    return sum([vec1[i]*vec2[i] for i in range(len(vec1))])
def GetLenght(vec):
    return (vec[0]**2+vec[1]**2)**0.5
def GetVektorTangent(point):
    return [1.,-4.*point[0]/point[1]]
    
def subvec(vec1,vec2):
    return [vec1[i]-vec2[i] for i in range(len(vec1))]
def NewVektor(linevec,tangentvec):
    lenght=GetLenght(tangentvec)
    substractvec=MultiplyVektor(tangentvec,2*dotproduct(linevec,tangentvec)/(lenght**2))
    return subvec(linevec,substractvec)
    
def GetIntersection(point,vektor):
    Roundprec=5
    slope=vektor[1]/vektor[0]
    x_0=point[0]
    y_0=point[1]
    b=-slope*x_0+y_0
    x_1=(-b*slope+2.*(-b**2+25.*slope**2+100.)**0.5)/(slope**2+4.)
    x_2=-(b*slope+2.*(-b**2+25.*slope**2+100.)**0.5)/(slope**2+4.)
    y_1=(-b*slope+2.*(-b**2+25.*slope**2+100.)**0.5)*slope/(slope**2+4.)+b
    y_2=-(b*slope+2.*(-b**2+25.*slope**2+100.)**0.5)*slope/(slope**2+4.)+b
    if round(x_1,Roundprec)==round(x_0,Roundprec) and round(y_1,Roundprec)==round(y_0,Roundprec):
        return [x_2,y_2]
    return [x_1,y_1]

def Draw(a,b,points,hits):
    ELIPSERECT=pygame.Rect((-a*30+SCREENSIZE[0]/2,-b*30+SCREENSIZE[1]/2.),(a*60,b*60))
    newpoints=[]
    for point in points:
        newpoints.append([point[0]*30+SCREENSIZE[0]/2.,point[1]*30+SCREENSIZE[1]/2.])
    screen.fill(BACKGROUNDCOLOR)
    pygame.draw.ellipse(screen,ELIPSECOLOR,ELIPSERECT,1)
    pygame.draw.aalines(screen,LINECOLOR,0,newpoints)
    text=font.render(str(hits)+" hits",True,(0,0,0))
    screen.blit(text,(0,0))
    pygame.display.flip()
    
    
pygame.init()
screen=pygame.display.set_mode(SCREENSIZE,0,32)
font = pygame.font.SysFont(FONTUSED, 32)
point=[1.4,-9.6]
vektor=NewVektor([1.4-0.,-9.6-10.1],GetVektorTangent([1.4,-9.6]))
hits=1
points=[[0.0,10.1],[1.4,-9.6]]
while(True):
    Draw(5,10,points,hits)
    time.sleep(.01)
    point=GetIntersection(point,vektor)
    points.append(point)
    if point[0]<0.01 and point[0]>-0.01:
        if point[1]>0:
            break
    vektor=NewVektor(vektor,GetVektorTangent(point))
    hits+=1
print hits

