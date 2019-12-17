import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

from queue import Queue


def get_cleaner(grid):
    for r, line in enumerate(grid):
        for c, ch in enumerate(line):
            if ch == '^':
                return r, c

    

def moveForward(pos, currDir, grid, R, C):
    cnt = 0 
    nextpos = pos[0] + currDir[0], pos[1] + currDir[1]
    while 0 <= nextpos[0] < R and 0 <= nextpos[1] < C and grid[nextpos[0]][nextpos[1]] == '#':
        pos = nextpos
        cnt += 1
        nextpos = pos[0] + currDir[0], pos[1] + currDir[1]
    
    leftOf = {(-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0)}
    rightOf = {(0, -1):(-1, 0), (1, 0):(0, -1), (0, 1):(1, 0), (-1, 0):(0, 1)}
    
    toLeft = pos[0] + leftOf[currDir][0], pos[1] + leftOf[currDir][1]
    toRight = pos[0] + rightOf[currDir][0], pos[1] + rightOf[currDir][1]
    newDir = (0, 0)
    s ='N'
    if 0 <= toLeft[0] < R and 0<= toLeft[1] < C and grid[toLeft[0]][toLeft[1]] == '#':
        newDir = leftOf[currDir]
        s = 'L'
    elif 0 <= toRight[0] < R and 0<= toRight[1] < C and grid[toRight[0]][toRight[1]] == '#':
        newDir = rightOf[currDir]
        s = 'R'
    return pos, newDir, s, cnt


def get_instructions(cleaner, grid):
    currDir = (-1, 0)
    pos = cleaner
    steps = []
    while currDir != (0, 0):
        pos, newDir, s, no_steps = moveForward(pos, currDir, grid, len(grid), len(grid[0]))
        if no_steps > 0:
            steps.append(no_steps)
        if s != 'N':
            steps.append(s)  
        currDir = newDir
    return steps  


def intersect(r, c):
    return (grid[r][c] == '#' and 
        grid[r-1][c] == '#' and
        grid[r+1][c] == '#' and
        grid[r][c-1] == '#' and
        grid[r][c+1] == '#')

grid = []
data = sys.stdin.readlines()
for line in data:
    grid.append(list(line.strip()))


cleaner = get_cleaner(grid)
inst = get_instructions(cleaner, grid)

s = ','.join(map(str, inst))
A = 'R,12,L,8,L,4,L,4'
B = 'L,8,R,6,L,6'
C = 'L,8,L,4,R,12,L,6,L,4'
prog = [A, B, A, B, C, A, C, A, C, B]
s2 = ','.join(prog)
print(s)
print(s2)
assert s == s2

