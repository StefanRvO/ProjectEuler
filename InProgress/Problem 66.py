def isSquare(num):
    square=num**0.5
    if square==int(square):
        return True
    return False

def FindMinimalx(D):
    minimalx=999999999
    if isSquare(D):
        return 10**10
    for i in range(1,10000):
        x=(1+D*i**2)**0.5
        if not x==int(x):
            continue
        if x<minimalx:
            minimalx=x
    return minimalx


for i in range(1000):
    print i,FindMinimalx(i)
