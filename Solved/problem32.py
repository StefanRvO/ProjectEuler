def ispandigital(mul1,mul2,prod):
    digitstring=str(mul1)+str(mul2)+str(prod)
    for char in "123456789":
        if not char in digitstring:
            return False
    return True

panprod=[]
for i in xrange(5000):
    for j in xrange(5000):
        if j>i:
            break
        prod=i*j
        if len(str(prod)+str(i)+str(j))>9:
            break
        elif ispandigital(i,j,prod):
            panprod.append(prod)
print sum(list(set(panprod)))
