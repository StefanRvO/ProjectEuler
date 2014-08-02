def isprime(num):
    if num<1:
        return False
    prime=0
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            prime=1
            break
    if prime==0:
        return True
    else:
        return False

i=0

for j in range(1,100000000,2):
    if isprime(j):
        i+=1
        if i==10001:
            print j
            break
