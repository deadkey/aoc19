import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
from collections import defaultdict as dd
import math

def gcd(a, b):
    if b == 0:
        return a
    if a == 0:
        return b
    return b if a % b == 0 else gcd(b, a % b)


def canSee(a, b, astset):
    r,c = a
    R, C = b
    dy = C -c
    dx = R -r
    g = gcd(abs(dy), abs(dx))
    jumpr = dx//g
    jumpc = dy//g
    
    for k in range(1, g):
        row, col = k * jumpr + r, k * jumpc + c
        if (row, col) in astset:
            return False
    return True

def canSee2(a, b, astset):
    r,c = a
    R, C = b
    dy = C -c
    dx = R -r
    g = gcd(abs(dy), abs(dx))
    jumpr = dx//g
    jumpc = dy//g
    angle = math.atan2(dy, -dx) % (2 * math.pi)
    no = 0
    
    for k in range(1, g):
        row, col = k * jumpr + r, k * jumpc + c
        if (row, col) in astset:
            no += 1
    return no, angle

def g(cnt, noR, noC, ast):
    for r in range(noR):
        out = []
        for c in range(noC):
            if (r, c) in ast:
                out.append(str(cnt[(r, c)]))
            else:
                out.append('.')
        print(''.join(out))
    

    


def p1(v, log=False):
    lines = v.strip().split('\n')
    grid = [[] for _ in range(len(lines))]
    ast = []
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            if ch == '.':
                grid[row].append(0)
            else:
                grid[row].append(1)
                ast.append((row, col))
    astset = set(ast)
    seen = dd(list)
    cnt = dd(int)
    for n in range(len(ast)):
        for other in range(len(ast)):
            if n != other:
                if canSee(ast[n], ast[other], astset):
                    cnt[(ast[n])] += 1
                    seen[ast[n]].append(ast[other])
    best = -1
    bestast = (-1, -1)
    #pp('testing', seen[(2,4)])
    #g(cnt, len(lines), len(lines[0]), ast)
    #pp(cnt)
    for n in range(len(ast)):
        if cnt[ast[n]] > best:
            best = cnt[ast[n]]
            bestast = ast[n]
    return best, bestast

def p2(v, log=False):
    lines = v.strip().split('\n')
    grid = [[] for _ in range(len(lines))]
    ast = []
    for row, line in enumerate(lines):
        for col, ch in enumerate(line):
            if ch == '.':
                grid[row].append(0)
            else:
                grid[row].append(1)
                ast.append((row, col))
    astset = set(ast)
    #station = (13, 11)
    station = (29, 26)
    so = []
    for i in range(len(ast)):
        if ast[i] != station:
            no, ang = canSee2(station, ast[i], astset)
            so.append((no, ang, ast[i]))
    so.sort()
    tr, tc = so[199][2]

    return tc * 100 + tr 

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
    PP = 1
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
