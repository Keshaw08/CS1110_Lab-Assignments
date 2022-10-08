# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 22:06:22 2022

@author: kesha
"""

class MainExecutor():
    
    pathRow = [2,1,-1,-2,-2,-1,1,2]
    pathCol = [1,2,2,1,-1,-2,-2,-1]
    
    visited = [[0 for i in range(8)] for j in range(8)]
    visited[0][0] = 1
    print("The Knight will move along the following path: \n")
    KnightTour(visited,0,0,1)
    
    def KnightTour(visited, row, col, move):
        if(move == 64):
            for i in range(8):
                for j in range(8):
                    if(visited[i][j] < 10):
                        visited[i][j] = str("0" + str(visited[i][j]))
                    print(f"{visited[i][j]} ",end=" ")
                print()
        else:
            for i in range(len(pathRow)):
                newRow = row + pathRow[i]
                newCol = col + pathCol[i]
                if(ifValidMove(visited,newRow,newCol)):
                    move+=1
                    visited[newRow][newCol] = move
                    if(KnightTour(visited,newRow,newCol,move)):
                        return True
                    move-=1
                    visited[newRow][newCol]=0 
        return False

    def ifValidMove(visited,newRow,newCol):
        if((newRow >= 0) and (newRow < 8) and (newCol >= 0) and (newCol < 8) and (visited[newRow][newCol]==0)):
            return True
        return False

executor = MainExecutor()
executor