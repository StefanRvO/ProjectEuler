#!/usr/bin/python


def tet(number,Power,mod=0):
    Rnumber=number
    while (Power>1):
        if mod:
            number=pow(Rnumber,number,mod)
        else:
            number=pow(Rnumber,number)  
        Power-=1
    return number
    
 
print tet(1777,1855,pow(10,8))
        
