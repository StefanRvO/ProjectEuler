#!/usr/bin/python
import gmpy2
summe=0
for i in xrange(10,150000000,10):
    if (i%3==0):
        continue
    if not(i%7==3 or i%7==4):
        continue
    if i%13==0:
        continue
    iSquare=i*i
    if not gmpy2.is_prime(iSquare+1):
        continue
    if not gmpy2.next_prime(iSquare+1)==iSquare+3:
        continue
    if not gmpy2.next_prime(iSquare+3)==iSquare+7:
        continue
    if not gmpy2.next_prime(iSquare+7)==iSquare+9:
        continue
    if not gmpy2.next_prime(iSquare+9)==iSquare+13:
        continue
    if not gmpy2.next_prime(iSquare+13)==iSquare+27:
        continue
    summe+=i
    print i
print summe
        
    
