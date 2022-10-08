# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 22:05:19 2022

@author: kesha
"""

class MainExecutor():
    def tictactoe(self):
        arr = []
        symbol = 0

        def logic(value, count):
            if(arr[value] == "X" or arr[value] == "O"):
                print(f"{value} this is Already Occupied.")
                symbol-=1
            else:
                if(count%2==0):
                    arr[value] = "X"
                else:
                    arr[value] = "O"
            print("|",arr[0],"|",arr[1],"|",arr[2],"|")
            print("|---|---|---|")
            print("|",arr[3],"|",arr[4],"|",arr[5],"|")
            print("|---|---|---|")
            print("|",arr[6],"|",arr[7],"|",arr[8],"|")
            print();
            
        def traverse():
            flag = True
            flagcount=0
            for i in range(9):
                if(arr[i] == "X" or arr[i]=="O"):
                    flagcount+=1
                    if(flagcount==9):
                        flag=False
                        break
                    elif(arr[i]!="X" or arr[i]!="O"):
                        flag = True
                        break
            return flag

        winner = False
        
        def winner():
            for i in range(3):
                if (arr[0+i]=="X" and arr[3+i]=="X" and arr[6+i]=="X" or arr[0+i]=="O" and arr[3+i]=="O" and arr[6+i]=="O"):
                    print(f"{arr[0+i]} is Winner")
                    flag = False
                    winner = True
                    break
            for i in range(7):
                if (arr[0+i]=="X" and arr[1+i]=="X" and arr[2+i]=="X" or arr[0+i]=="O" and arr[1+i]=="O" and arr[2+i]=="O"):
                    print(f"{arr[0+i]} is Winner")
                    flag = False
                    winner = True
                    break
            if (arr[0]=="X" and arr[4]=="X" and arr[8]=="X" or arr[0]=="O" and arr[4]=="O" and arr[8]=="O"):
                print(f"{arr[0]} is Winner")
                flag = False
                winner = True
            elif(arr[2]=="X" and arr[4]=="X" and arr[6]=="X" and arr[2]=="O" and arr[4]=="O" and arr[6]=="O"):
                print(f"{arr[2]} is Winner")
                flag = False
                winner = True
                
        def isMoveLeft(arr):
            for i in range(9):
                if(arr[i] != "X" or arr[i]!="O"):
                    return True
            return False
        
        for i in range(9):
            arr.append(str(i))
        print("|",arr[0],"|",arr[1],"|",arr[2],"|")
        print("|---|---|---|")
        print("|",arr[3],"|",arr[4],"|",arr[5],"|")
        print("|---|---|---|")
        print("|",arr[6],"|",arr[7],"|",arr[8],"|")

        while(traverse()):
            if(symbol%2==0):
                print("Enter the number where you want to place X at: ")
            else:
                print("Enter the number where you want to place O at: ")
            logic(int(input()),symbol)
            symbol+=1
            winner()
            if(winner == False):
                print("TicTacToe is DRAW.")
                
executor = MainExecutor()
executor.tictactoe()