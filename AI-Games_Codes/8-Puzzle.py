#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

initialmatrix=np.array([['2','8','3'],['1','6','4'],['7',' ','5']])
finalmatrix=np.array([['1','2','3'],['8',' ','4'],['7','6','5']])
grid=initialmatrix

print("Initial Configuration : \n")
print(initialmatrix)

print("\nFinal Configuration: \n")
print(finalmatrix)
print()

def Moves(i,j):
    return [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]

def isSafe(i,j):
    return i>=0 and i<3 and j>=0 and j<3

def calManhattan(grid):
    sum=0
    for i in range(3):
        for j in range(3):
            if grid[i][j]!=' ':
                sum = sum+abs(i-np.where(finalmatrix==grid[i][j])[0][0])+abs(j-np.where(finalmatrix==grid[i][j])[1][0])
    return sum

def solve(blankR, blankC):
    global grid
    if np.array_equal(grid,finalmatrix):
        return

    manhattanDistance=[]
    for move in Moves(blankR,blankC):
        if isSafe(move[0],move[1]):
            grid[move[0]][move[1]],grid[blankR][blankC]=grid[blankR][blankC],grid[move[0]][move[1]]
            manhattanDistance.append([calManhattan(grid),grid.copy(),move[0],move[1]])
            grid[move[0]][move[1]],grid[blankR][blankC]=grid[blankR][blankC],grid[move[0]][move[1]]

    manhattanDistance.sort(key = lambda manhattanDistance: manhattanDistance[0])
    grid=manhattanDistance[0][1]
    print(grid)
    print()
    solve(manhattanDistance[0][2],manhattanDistance[0][3])

print("SOLUTION: \n")
solve(2,1)


# In[ ]:




