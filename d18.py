import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
from collections import defaultdict as dd

sys.setrecursionlimit(10000)

            
def getReach(grid, fromPos, letters):
    keys = set()
    visited = {}
    visited[fromPos] = 0
    q = [fromPos]
    while q:
        q2 = []
        for pos in q:
            dirs =[(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in dirs:
                pr, pc = pos[0]+ dr, pos[1] + dc
                if ((grid[pr][pc] == '.' and 
                    (pr, pc) not in visited) or
                    (ord('a') <= ord(grid[pr][pc]) <= ord('z') and grid[pr][pc] not in letters)):
                    visited[(pr, pc)] = visited[pos] + 1
                    q2.append((pr, pc))
                if grid[pr][pc] in letters:
                    keys.add((grid[pr][pc], pr, pc, visited[pos] + 1))
                if (ord('A') <= ord(grid[pr][pc]) <= ord('Z') and 
                    grid[pr][pc].lower() not in letters and
                    (pr, pc) not in visited):
                    visited[(pr, pc)] = visited[pos] + 1
                    q2.append((pr, pc))
                    
        q = q2
    return keys

def getReachAll(grid, fromPos, letters):
    keys = set()
    visited = {}
    for _p in fromPos:
        visited[_p] = 0
    q = [(pp[0], pp[1], i) for i, pp in enumerate(fromPos)]
    while q:
        q2 = []
        for posR, posC, i in q:
            dirs =[(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dr, dc in dirs:
                pr, pc = posR+ dr, posC + dc
                if (pr, pc) in visited:
                    continue
                if grid[pr][pc] == '.' or (ord('a') <= ord(grid[pr][pc]) <= ord('z') and grid[pr][pc] not in letters):
                    visited[(pr, pc)] = visited[(posR, posC)] + 1
                    q2.append((pr, pc, i))
                
                elif grid[pr][pc] in letters:
                    keys.add((grid[pr][pc], pr, pc, visited[(posR, posC)] + 1, i))
                elif (ord('A') <= ord(grid[pr][pc]) <= ord('Z') and 
                    grid[pr][pc].lower() not in letters and
                    (pr, pc) not in visited):
                    visited[(pr, pc)] = visited[(posR, posC)] + 1
                    q2.append((pr, pc, i))
                
        q = q2
    return keys


def find(grid, ch):
    keys = []
    start = -1, -1
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == ch:
                start=  r, c
                grid[r][c] = '.'
            if ord('a') <= ord(grid[r][c]) <= ord('z'):
                keys.append(grid[r][c])
    return start, keys


def findAll(grid, ch):
    keys = []
    start = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == ch:
                start = [(r-1, c-1), (r-1, c+1), (r+1, c-1), (r+1, c+1)]
                grid[r][c] = '#'
                grid[r][c+1] = '#'
                grid[r][c-1] = '#'
                grid[r-1][c] = '#'
                grid[r+1][c] = '#'

            if ord('a') <= ord(grid[r][c]) <= ord('z'):
                keys.append(grid[r][c])
    return start, keys

def inf():
    return 10 ** 12

def solve(fromPos, grid, lettersLeft, DP):
    if DP[fromPos, lettersLeft] != 10 ** 12:
        return DP[fromPos, lettersLeft]
    if len(lettersLeft) == 0:
        return 0
    reachableKeys = getReach(grid, fromPos, lettersLeft)
    pp('In solve', fromPos, reachableKeys, lettersLeft)
    
    for key in reachableKeys:
        
        k, r, c, dist = key
        pp('Checking ', fromPos, k, lettersLeft)
        if k in lettersLeft:
            nLetters = lettersLeft.replace(k, '')
            pos = r, c
            alt = solve(pos, grid, nLetters, DP) + dist
            pp('alt', k, alt, dist)
            DP[fromPos, lettersLeft] = min(DP[fromPos, lettersLeft], alt)
    pp('Res', grid[fromPos[0]][fromPos[1]], fromPos, lettersLeft, DP[fromPos, lettersLeft])
    return DP[fromPos, lettersLeft]

def solveAll(fromPos, grid, lettersLeft, DP):
    if DP[tuple(fromPos), lettersLeft] != 10 ** 12:
        return DP[tuple(fromPos), lettersLeft]
    if len(lettersLeft) == 0:
        return 0
    reachableKeys = getReachAll(grid, fromPos, lettersLeft)
    #if len(lettersLeft) >= 20:
    #    pp('LettersLeft', len(lettersLeft))
    for key in reachableKeys:
        
        k, r, c, dist, i = key
        if k in lettersLeft:
            nLetters = lettersLeft.replace(k, '')
            pos2 = [pos for pos in fromPos]
            pos2[i]  = (r, c)
            alt = solveAll(pos2, grid, nLetters, DP) + dist
            DP[tuple(fromPos), lettersLeft] = min(DP[tuple(fromPos), lettersLeft], alt)
    return DP[tuple(fromPos), lettersLeft]

def p1(v, log=False):
    lines = v.strip().split('\n')
    grid = []
    for line in lines:
        grid.append(list(line))
    start, keys = find(grid, '@')
    
    lettersLeft = ''.join(sorted(keys))
    DP = dd(inf)
    solve(start, grid, lettersLeft, DP)


    return DP[start, lettersLeft]

def p2(v, log=False):
    
    lines = v.strip().split('\n')
    grid = []
    for line in lines:
        grid.append(list(line))
    start, keys = findAll(grid, '@')
    
    lettersLeft = ''.join(sorted(keys))
    DP = dd(inf)
    solveAll(start, grid, lettersLeft, DP)


    return DP[tuple(start), lettersLeft]
    

def pp(*v):
    if PP:
        print(v) 

def get_day():
    return 18

def get_year():
    return 2019



if __name__ == '__main__':
    #0 samples_only, 1 run everything, 2 only my input data
    DB = 2
    #Debugprint: print if 1, not if 0
    PP = 0
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
