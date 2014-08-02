alphabet="abcdefghijklmnopqrstuvwxyz"

def loadwords():
    file=open('words.txt')
    words=file.read()
    words=words.split('","')
    words[0]=words[0][1:]
    words[-1]=words[-1][:-1]
    return words

def getWordValue(word):
    global alphabet
    summe=0 
    for letter in word.lower():
        summe+=alphabet.index(letter)+1
    return summe
   
def TriangleNumber(n):
    return n*(n+1)/2

words=loadwords()
TriangleNumbers=[TriangleNumber(i) for i in range(1,100)]
counter=0
for word in words:
    if getWordValue(word) in TriangleNumbers:
        counter+=1
print counter

