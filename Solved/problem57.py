def gcd(x,y):
    k=0
    x_next=0;
    while(True):
        x_next=y
        y=x%y
        x=x_next
        if(y==0):
            return x
            
def ReduceFrac(frac):
    gcdfrac=gcd(frac[0],frac[1])
    frac[0]/=gcdfrac
    frac[1]/=gcdfrac
    return frac
def SquareCon2(n=1,frac=[2,1]):
    if n==1 and frac!=[2,1]:
        PrevConverg=[frac[0]+frac[1],frac[1]]
        PrevConverg=[PrevConverg[1],PrevConverg[0]]
        PrevConverg[0]+=PrevConverg[1]
        return PrevConverg
    PrevConverg=frac
    while(n>1):
        n-=1
        PrevConverg=[PrevConverg[1],PrevConverg[0]]
        PrevConverg[0]+=2*PrevConverg[1]
    PrevConverg=[PrevConverg[1],PrevConverg[0]]
    PrevConverg[0]+=PrevConverg[1]
    return PrevConverg
    
    
counter=0
fract=SquareCon2()
for i in range(1000):
    if len(str(fract[0]))>len(str(fract[1])):
        counter+=1
    fract=SquareCon2(frac=fract)
print counter
