ones=[4,3,3,5,4,4,3,5,5,4]
teens=[3,6,6,8,8,7,7,9,8,8]
teeeens=[0,0,6,6,5,5,5,7,6,6]
thousand=8+3
hundred=7
_and=3


def getLetterCount(n):
    global ones,teens,teeeens,thousand,hundred,hundredand
    if n==1000:
        return thousand
    if n<10:
        return ones[n]
    if n<20:
        return teens[n%10]
    if n<100:
        if n%10==0:
            return teeeens[n/10]
        return teeeens[n/10]+ones[n%10]
    digit2=n%100
    
    lettersum=ones[n/100]+hundred
    if digit2==0:
        return lettersum
    lettersum+=_and
    if digit2<10:
        return ones[digit2]+lettersum
    if digit2<20:
        return teens[digit2%10]+lettersum
    if digit2%10==0:
        return teeeens[digit2/10]+lettersum
    return teeeens[digit2/10]+ones[digit2%10]+lettersum
    
sumlist=[]
for i in range(1,1001):
    sumlist.append(getLetterCount(i))
    
print sum(sumlist)
