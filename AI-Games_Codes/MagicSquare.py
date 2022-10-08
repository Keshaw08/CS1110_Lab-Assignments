import numpy as np

def magic_square_upright():
    n = int(input("Enter the size of matrix : "))
    arr1 = [[0 for x in range(n)] for y in range(n)]
    arr = np.array(arr1)
    row = 0
    col = n//2
    arr[row,col] = 1
    constant = int(n*(n**2 + 1)/2)
    
    for num in range(2,n*n+1):
        row-=1
        col+=1
        if(col == n):
            col = 0
        elif(row == -1):
            row = n-1
        if((row==-1 and col==n) or (arr[row,col] != 0)):
            row+=2
            col-=1
        arr[row,col] = num
    print("Constant value : ",constant,"\n")
    print(arr)

magic_square_upright()