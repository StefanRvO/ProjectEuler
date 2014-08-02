def loadmatrix():
    file=open('matrix.txt')
    matrix=file.read()
    matrix=matrix.split('\n')[:-1]
    for i in range(len(matrix)):
        matrix[i]=matrix[i].split(',')
        for j in range(len(matrix[i])):
            matrix[i][j]=int(matrix[i][j])
    return matrix

def findShortestpath(x,y):
    global matrix
    global emptymatrix
    if emptymatrix[x][y]!='':
        pass
    elif x==len(matrix) and y==x:
        emptymatrix[x][y]=matrix[x][y]
    elif x==len(matrix)-1:
        emptymatrix[x][y]=matrix[x][y]+findShortestpath(x,y+1)
    elif y==len(matrix)-1:
        emptymatrix[x][y]=matrix[x][y]+findShortestpath(x+1,y)
    else:
        emptymatrix[x][y]=matrix[x][y]+min([findShortestpath(x,y+1),findShortestpath(x+1,y)])
    return emptymatrix[x][y]
           
            
    
    
matrix=loadmatrix()
#matrix=[[2421,131,673,234,245,103,18],[201,426,96,342,965,150,53245],[630,80,3,746,422,111,231],[53,7,699,497,121,956,6],[805,732,5,24,37,331,4],[131,673,23,4,103,18,3],[2421,131,673,234,245,103,18]]
emptymatrix=[['' for i in range(len(matrix))] for j in range(len(matrix))]
emptymatrix[-1][-1]=matrix[-1][-1]

print findShortestpath(0,0)


