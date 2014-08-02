#!/usr/bin/python
integerstring=''
i=1

while(len(integerstring)<=1000000):
    integerstring+=str(i)
    i+=1
    

prod=1
for i in [1,10,100,1000,10000,100000,1000000]:
    prod*=int(integerstring[i-1])
print prod
