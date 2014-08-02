def divisorsum(number):    #returns a list of divisors
    divisors=[1]
    if number%2!=0:
        for i in range(3,int(number**0.5)+1,2):
            if number%i==0:
                divisors.append(i)
                divisors.append(number/i)
    else:
        for i in range(2,int(number**0.5)+1):
            if number%i==0:
                divisors.append(i)
                divisors.append(number/i)
    return sum(list(set(divisors)))
        

def isAmicable(number):
    divisorpair=divisorsum(number)
    if divisorpair==number:
        return False
    if number==divisorsum(divisorpair):
        return True
    return False


summe=0
for i in range(1,10000):
    if isAmicable(i):
        summe+=i
print summe

