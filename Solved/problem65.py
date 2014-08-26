def timesfrac(frac,n):
    return [frac[0]*n,frac[1]*n]
    
def fracadd(frac1,frac2):
    if frac1[0]==0:
        return frac2
    elif frac2[0]==0:
        return frac1
    detmp=frac1[1]
    frac1=timesfrac(frac1,frac2[1])
    frac2=timesfrac(frac2,detmp)
    return [frac1[0]+frac2[0],frac1[1]]

n=100
x=0
frac=[0,1]
for i in range(n+1,0,-1):
    if i%3==1:
        j=[(i/3)*2,1]
    else:
        j=[1,1]
    frac=fracadd(frac,j)[::-1]
    
print sum([int(i) for i in str(frac[0]+frac[1])])
