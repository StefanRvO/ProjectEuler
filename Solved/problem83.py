#!/usr/bin/python
def loadmatrix():
    file=open('matrix.txt')
    matrix=file.read()
    matrix=matrix.split('\n')[:-1]
    for i in range(len(matrix)):
        matrix[i]=matrix[i].split(',')
        for j in range(len(matrix[i])):
            matrix[i][j]=int(matrix[i][j])
    return matrix



def GetHmatrix(matrix,end):
    #Find the lovest value in the matrix
    H_matrix=[['' for i in range(len(matrix))] for j in range(len(matrix))]
    summe=0
    for i in matrix:
        for j in i:
            summe+=j
    avg=summe/(len(matrix)**2)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            H_matrix[i][j]=(abs(i-end[0])+abs(j-end[1])+1)*int((avg**0.5))
    
    return H_matrix

def GetAdjecentSquares(placement):
    global matrix
    Squares=[]
    if not placement[0]==0:
        Squares.append([placement[0]-1,placement[1]])
    if not placement[1]==0: 
        Squares.append([placement[0],placement[1]-1])
    if not placement[0]==len(matrix)-1:
        Squares.append([placement[0]+1,placement[1]])
    if not placement[1]==len(matrix)-1:
        Squares.append([placement[0],placement[1]+1])
    return Squares
    
def FindGValue(placement,parent=0):
    global G_matrix
    global ParentSquares
    if parent==0:
        parent=ParentSquares[placement[0]][placement[1]]
    if parent==placement:
        return G_matrix[parent[0]][parent[1]]
    if G_matrix[parent[0]][parent[1]]=='':
        return matrix[placment[0]][placement[1]]+FindGValue(parent)
    return matrix[placement[0]][placement[1]]+G_matrix[parent[0]][parent[1]]
    
def FindFValue(placement,force=False):
    global F_matrix
    global G_matrix
    global H_matrix
    if F_matrix[placement[0]][placement[1]]=='' or force:
        if G_matrix[placement[0]][placement[1]]=='' or force:
            G_matrix[placement[0]][placement[1]]=FindGValue(placement)
        F_matrix[placement[0]][placement[1]]=G_matrix[placement[0]][placement[1]]+H_matrix[placement[0]][placement[1]]
    return F_matrix[placement[0]][placement[1]]
def FindLowestF():
    global OpenList
    lowest=999999999999999
    lowplacement=''
    for placement in OpenList:
        cur=FindFValue(placement)
        if cur<lowest:
            lowest=cur
            lowplacement=placement
    return lowplacement
def GetBackPath(placement,start):
    global ParentSquares
    if placement==start:
        return [placement]
    
    return [placement]+GetBackPath(ParentSquares[placement[0]][placement[1]],start)
def A_Star(start,end,matrix):  
    H_matrix=GetHmatrix(matrix,end)
    global G_matrix
    global F_matrix
    global H_matrix
    global ClosedList
    global OpenList
    global ParentSquares
    OpenList.append(start)
    while True:
        placement=FindLowestF()
        OpenList.remove(placement)
        ClosedList.append(placement)
        if placement==end:
            break
        adjecentsquares=GetAdjecentSquares(placement)
        for square in adjecentsquares:
            if square in ClosedList:
                continue
            if not square in OpenList:
                OpenList.append(square)
                ParentSquares[square[0]][square[1]]=placement
                FindFValue(square)
            else:
                if FindGValue(square,placement)<G_matrix[square[0]][square[1]]:
                    ParentSquares[square[0]][square[1]]=placement
                    FindFValue(square)
    Path=GetBackPath(end,start)
    return Path
        

matrix=loadmatrix()
#matrix=[[131,673,234,103,18],[201,96,342,965,150],[630,803,746,422,111],[537,699,497,121,956],[805,732,524,37,331]]
start=[0,0]
end=[len(matrix)-1,len(matrix)-1]
OpenList=[]
ClosedList=[]
G_matrix=[['' for i in range(len(matrix))] for j in range(len(matrix))]
G_matrix[start[0]][start[1]]=matrix[start[0]][start[1]]
F_matrix=[['' for i in range(len(matrix))] for j in range(len(matrix))]
H_matrix=GetHmatrix(matrix,end)
ParentSquares=[['' for i in range(len(matrix))] for j in range(len(matrix))]
ParentSquares[start[0]][start[1]]=start
bestpath= A_Star(start,end,matrix)

summe=0
for placement in bestpath:
    summe+=matrix[placement[0]][placement[1]]
print summe
