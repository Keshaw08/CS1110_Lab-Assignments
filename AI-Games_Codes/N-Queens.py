# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 22:05:53 2022

@author: kesha
"""

class MainExecutor():
    
    def __init__(self,n):
        self.n = n
        
    def is_Queen_safe(self,board, row, col, n):
        for c in range(col,-1,-1): 
            if board[row][c]==1:return False
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j]==1:return False
            i -=1
            j -=1
        i = row
        j = col
        while i < n and j >= 0:
            if board[i][j]==1: return False 
            i += 1
            j -= 1 
        return True

    def nQueens(self, board, col, n):
        if (col == n):return True
        for row in range(n):
            if(self.is_Queen_safe(board, row , col, n)):
                board[row][col] = 1
                if(self.nQueens(board, col+1,n)):return True
                board[row][col] = 0
        return False
    
    def createBoard(self):
        board = [[0 for i in range(n)] for j in range(n)]
        if self.nQueens(board, 0, n)==True: 
            print()
            for row in range(n): 
                for col in range(n) :
                    print(board[row][col], end = '| ') 
                print()
        else:print(f"N-Queens is not possible for given size: {n}")

n = int(input("Enter the size of Board : "))
executor = MainExecutor(n)
executor.createBoard()