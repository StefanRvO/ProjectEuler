def ispalindrome(num):
    numstr=str(num)
    for i in xrange(len(numstr)/2):
        if not numstr[-(i+1)]==numstr[i]:
            return False
    return True

palindromes=[]
for i in range(100,1000):
    for j in range(100,1000):
        if j>i:
            break
        if ispalindrome(i*j):
            palindromes.append(i*j)
print max(palindromes)
