#!/usr/bin/python

def GetSquareReminder(a,n):
    if n%2==0:
        return 2
    else:
        return (2*a*n)%(a**2)

def GetRmax(a):
    return 2*a*((a-1)/2)
print sum([GetRmax(a) for a in range(3,1001)])
#plt.plot(x,y)
#plt.show()
