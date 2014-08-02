#!/usr/bin/python

def loadgrid():
    file=open('grid.txt')
    grid=file.read()
    grid=grid.split('\n')[:-1]
    for i in range(len(grid)):
        grid[i]=grid[i].split(' ')
        for j in range(len(grid[i])):
            grid[i][j]=int(grid[i][j])
    return grid

Grid=loadgrid()
products=[]
for i in range(len(Grid)):
    for j in range(len(Grid)):
        if not i<=2:
            products.append(Grid[i][j]*Grid[i-1][j]*Grid[i-2][j]*Grid[i-3][j]) #up
        if not i>=len(Grid)-3:
            products.append(Grid[i][j]*Grid[i+1][j]*Grid[i+2][j]*Grid[i+3][j]) #down    
        if not j<=2: #left
            products.append(Grid[i][j]*Grid[i][j-1]*Grid[i][j-2]*Grid[i][j-3]) #left  
        if not j>=len(Grid)-3:
            products.append(Grid[i][j]*Grid[i][j+1]*Grid[i][j+2]*Grid[i][j+3]) #right
            if not i<=2:
                products.append(Grid[i][j]*Grid[i-1][j+1]*Grid[i-2][j+2]*Grid[i-3][j+3]) #right up
            if not i>=len(Grid)-3:
                products.append(Grid[i][j]*Grid[i+1][j+1]*Grid[i+2][j+2]*Grid[i+3][j+3]) #right down
                
                
print max(products)
