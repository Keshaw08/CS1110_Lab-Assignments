# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 22:04:10 2022

@author: kesha
"""

import pandas as pd
import numpy as np

class MainExecuter:
    n = 9
    def __init__(self,arr):
        self.arr = arr
    
    def solve(self,arr,row,col):
        if(row==n-1 and col==n):
            return True
        if(col==n):
            row+=1
            col=0
        if(self.arr[row][col] !=0):
            return self.solve(self.arr,row,col+1)
        for i in range(1,10):
            if(self.isSafe(arr,row,col,i)):
                self.arr[row][col] = i
                if(self.solve(self.arr,row,col+1)):
                    return True
            self.arr[row][col]=0
        return False

    def isSafe(self,arr,row,col,num):
        for i in range(0,9):
            if(self.arr[row][i]==num):
                return False
        for i in range(0,9):
            if(self.arr[i][col] == num):
                return False
        startRow = row - row%3
        startCol = col - col%3
        for i in range(3):
            for j in range(3):
                if (self.arr[i + startRow][j + startCol] == num):
                    return False
        return True
    
    
    def start_Solving(self):
        if(self.solve(self.arr,0,0)):
            print("The Solution for the given unsolved Sudoku: \n")
            for i in range(n):
                for j in range(n):
                    print(self.arr[i][j],end=" | ")
                print()
        else:
            println("NO Solution exist for the given Sudoku")
    
arr1 = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

arr = np.array(arr1)

executer = MainExecuter(arr)
executer.start_Solving()