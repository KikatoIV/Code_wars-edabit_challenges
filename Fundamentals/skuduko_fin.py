import numpy as np
from random import shuffel

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,0,0]]


def possible(x,y,n):
#this bit of code checks if there is any number similair to the one perposed
    for i in range(9):
        if grid[x][i] == n:
            return False
    for i in range(9):
        if grid[i][y] == n:
            return False
#There is a rule that every 3x3 block cant contain double this bit of code
#checks if there are any doubles
    xsqr = (x//3)*3
    yspr = (y//3)*3
    for i in range(0, 3):
        for j in range(0, 3):
            if grid[xsqr + i][yspr + j] == n:
                return False
    return True

def solve(grid):
    for x in range(9):
        for y in range(9):
            if grid[x][y]==0:
                for n in range(10):
                    if possible(x,y,n):
                        grid[x][y] = n
                        solve(grid)
                        grid[x][y] = 0
                return
                input()
    print(np.matrix(grid))


solve(grid)
