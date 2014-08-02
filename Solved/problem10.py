def isprime(num):
    if num<1:
        return False
    prime=0
    if num==2:
        return True
    if num%2==0:
        return False
    for i in range(3,int(num**0.5)+1,2):
        if num%i==0:
            prime=1
            break
    if prime==0:
        return True
    else:
        return False

summe=2
for i in range(3,2000000,2):
    if isprime(i):
        summe+=i
print summe
