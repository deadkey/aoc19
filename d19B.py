import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run


def p1(v, log=False):
    return 0

def check(r, c, grid):
    N = 100 #change this!
    for rr in range(r, r+N):
        for cc in range(c, c+ N):
            if rr >= len(grid) or cc >= len(grid[0]):
                return 10 ** 12, -1, -1
            if grid[rr][cc] == 0:
                return 10 ** 12, -1, -1
    #ok!
    return r + c, r, c

def p2(v, log=False):
    lines = sys.stdin.readlines()
    grid =[]
    pos = set()
   
    for r, line in enumerate(lines):
        L = []
        for c, ch in enumerate(line.strip()):
            if ch != '0':
                
                pos.add((r, c))
                L.append(1)
            else:
                L.append(0)
        if len(L) > 0:    
            grid.append(L)
    minDist = 10 ** 12,10000, 10000
    print(max(l.count('1') for l in lines))
    for r, c in pos:
        res = check(r, c, grid)
        minDist = min(minDist, res)
    print(minDist)
    return minDist[1] * 10000 + minDist[2]

def pp(*v):
    if PP:
        print(v) 

def get_day():
    return date.today().day

def get_year():
    return date.today().year



if __name__ == '__main__':
    #0 samples_only, 1 run everything, 2 only my input data
    DB = 2
    #Debugprint: print if 1, not if 0
    PP = 0
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
