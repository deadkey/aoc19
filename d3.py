import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

def p1(v, log=False):
    lines = v.strip().split('\n')
    grid = {}
    dmap = {'R': (0, 1), 'U': (-1,0), 'D': (1,0), 'L': (0,-1)}
    #wire 1
    dirs1 = lines[0].split(',')
    dirs2 = lines[1].split(',')
    cr, cc = 0,0
    for d in dirs1:
        D = d[0]
        steps = int(d[1:])
        for s in range(steps):
            dr, dc = dmap[D]
            cr, cc = cr + dr, cc + dc
            grid[(cr, cc)] = 1
    cr, cc = 0,0
    closest = 10 ** 12
    for d in dirs2:
        D = d[0]
        steps = int(d[1:])
        for s in range(steps):
            dr, dc = dmap[D]
            cr, cc = cr + dr, cc + dc
            if (cr, cc) in grid:
                closest = min(closest, abs(cr) + abs(cc))
            grid[(cr, cc)] = 2
    return closest
    




def p2(v, log=False):
    lines = v.strip().split('\n')
    steps1 = {}
    steps2 = {}
    
    dmap = {'R': (0, 1), 'U': (-1,0), 'D': (1,0), 'L': (0,-1)}
    #wire 1
    dirs1 = lines[0].split(',')
    dirs2 = lines[1].split(',')
    cr, cc = 0,0
    tot_steps= 0
    
    for d in dirs1:
        D = d[0]
        steps = int(d[1:])
        for s in range(steps):
            dr, dc = dmap[D]
            tot_steps += 1
            cr, cc = cr + dr, cc + dc
            
            if (cr, cc) not in steps1:
                steps1[(cr, cc)]= tot_steps
    cr, cc = 0,0
    closest = 10 ** 12
    tot_steps= 0
    for d in dirs2:
        D = d[0]
        steps = int(d[1:])
        for s in range(steps):
            dr, dc = dmap[D]
            cr, cc = cr + dr, cc + dc
            tot_steps += 1
            if (cr, cc) not in steps2:
                steps2[(cr, cc)]= tot_steps
            if (cr, cc) in steps1:
                closest = min(closest, steps1[(cr, cc)] + steps2[(cr, cc)])

    return closest

def get_day():
    return 3

def get_year():
    return 2019

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
