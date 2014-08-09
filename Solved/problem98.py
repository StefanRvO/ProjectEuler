#!/usr/bin/python
from itertools import permutations,combinations
def GetPosIntegersDupli(word,chartonumber,used,recur=1):
    integers=[]
    if recur:
        if len(word)==1:
            if word[0] in chartonumber[0]:
                return [chartonumber[1][chartonumber[0].index(word[0])]]
            else:
                return [char for char in ['1','2','3','4','5','6','7','8','9'] if not char in used]
        else:
            if word[0] in chartonumber[0]:
                integers+=[chartonumber[1][chartonumber[0].index(word[0])]+nextchar for nextchar in GetPosIntegersDupli(word[1:],chartonumber,used)]
            else:
                for char in "0123456789":
                    if not char in used:
                        integers+= [char+nextchar for nextchar in GetPosIntegersDupli(word[1:],[chartonumber[0]+[word[0]],chartonumber[1]+[char]],used+[char])]
            return integers
    else:
        for char in "123456789":
            if not char in used:
                integers+= [char+nextchar for nextchar in GetPosIntegersDupli(word[1:],[[word[0]],[char]],used+[char])]
        return integers
def GetPosIntegers(word,used,recur=1):
    global AllSquares
    
    return [str(x) for x in AllSquares if len(str(x))==len(word)]
    integers=[]
    if recur:
        if len(word)==1:
            return [char for char in ['1','2','3','4','5','6','7','8','9'] if not char in used]
        else:
            for char in "0123456789":
                if not char in used:
                    integers+= [char+nextchar for nextchar in GetPosIntegers(word[1:],used+[char])]
            return integers
    else:
        for char in "123456789":
            if not char in used:
                integers+= [char+nextchar for nextchar in GetPosIntegers(word[1:],used+[char])]
        return integers
def LargestPosSquare(Anagram):
    word1=Anagram[0]
    word2=Anagram[1]
    posintegers=[]
    dupli=False
    for char in word1:
        if word1.count(char)>=2:
            dupli=True
    if dupli:
        Posint=GetPosIntegersDupli(word1,[[],[]],[],0)
    else:
        Posint=GetPosIntegers(word1,[],0)
    Squares=[]
    for Integer in Posint:
        if isSquare(int(Integer)):
            Squares.append(Integer)
    Integers2=[]
    for i in range(len(Squares)):
        Integers2.append('')
        for j in range(len(word1)):
            index=list(word1).index(word2[j])
            Integers2[i]+=Squares[i][index]
        Squares[i]=int(Squares[i])
    FinalSquares=[]
    for i in range(len(Integers2)):
        if isSquare(int(Integers2[i])):
            if len(str(int(Integers2[i])))==len(str(Squares[i])):
                FinalSquares.append(int(Integers2[i]))
                FinalSquares.append(Squares[i])
    FinalSquares.append(0)
    return max(FinalSquares)
def isSquare(n):
    square=n**0.5
    if int(square)==round(square,5):
        return True
    return False
def loadwords():
    file=open('words.txt')
    words=file.read()
    words=words.split('","')
    words[0]=words[0][1:]
    words[-1]=words[-1][:-1]
    return words

def GetAnagrams(words):
    Anagrams=[]
    for word in words:
        Anagram=[]
        if len(word)>6:
            for thisword in words:
                if len(thisword)==len(word):
                    if all([thisword.count(char)==word.count(char) for char in word]):
                        Anagram.append(thisword)
        else:
            wordpermu=[ "".join(x) for x in permutations(word)]
            for permu in wordpermu:
                if permu in words and ( permu not in Anagram):
                    Anagram.append(permu)
        if len(Anagram)>=2:
            Anagram.sort()
            if Anagram not in Anagrams:
                Anagrams.append(Anagram)
    for Anagram in Anagrams:
        if len(Anagram)>2:
            Anagrams.remove(Anagram)
            Anagrams+=list(combinations(Anagram,2))
    return Anagrams

words=loadwords()
Anagrams=GetAnagrams(words)
maxlen=max([len(Anagram[0]) for Anagram in Anagrams])
AllSquares=[]
lastsquare=0
i=0
while len(str(lastsquare))<=maxlen:
    i+=1
    lastsquare=i*i
    AllSquares.append(str(lastsquare))
startlen=0
endlen=1
while startlen!=endlen:
    startlen=len(AllSquares)
    for square in AllSquares:
        for integer in xrange(10):
            if list(str(square)).count(str(integer))>1:
                AllSquares.remove(square)
                break
    endlen=len(AllSquares)
    
print max([LargestPosSquare(Anagram) for Anagram in Anagrams])
