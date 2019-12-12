import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
import re

def apply_grav(moons, vels):
    
    for i in range(len(moons)):
        for j in range(len(moons)):
            if i != j:
                for coord in range(3):
                    diff = 0
                    if (moons[j][coord] - moons[i][coord])> 0:
                        diff =1
                    if (moons[j][coord] - moons[i][coord]) < 0:
                        diff = -1
                    vels[i][coord] += diff
    return vels


def apply_vel(moons, vels):
    pos = [[0] * 3 for _ in range(4)]
    
    for i in range(len(moons)):
        
        newpos = moons[i]
        for coord in range(3):
            newpos[coord] = moons[i][coord] + vels[i][coord]
        pos[i] = newpos
    return pos

def energy(moons, vels):
    p =0
    for i in range(4):
        pot = 0
        kin = 0
        for coord in range(3):
            pot += abs(moons[i][coord])
            kin += abs(vels[i][coord])
        p += pot * kin
    return p


def grav(moons, vels, coord):
    
    for i in range(len(moons)):
        for j in range(len(moons)):
            if i != j:
                diff = 0
                if (moons[j][coord] - moons[i][coord])> 0:
                    diff =1
                if (moons[j][coord] - moons[i][coord]) < 0:
                    diff = -1
                vels[i][coord] += diff
    return vels


def vel(moons, vels, coord):
    pos = [[0] * 3 for _ in range(4)]
    
    for i in range(len(moons)):
        
        newpos = moons[i]
        newpos[coord] = moons[i][coord] + vels[i][coord]
        pos[i] = newpos
    return pos



def p1(v, log=False):
    lines = v.strip().split('\n')
    moons = []
    for line in lines:
        x,y, z = map(int, re.sub("[^0-9- ]", "", line).split())
        moons.append([x, y, z])
    vels = [[0] * 3 for _ in range(4)]
         
    N = 1000 #change this!

    for t in range(N):
        #apply gravity
        vels = apply_grav(moons, vels)
        moons = apply_vel(moons,vels)
        pp('Step {}'.format(t + 1))
        pp(moons)
        pp(vels)
        #apply vel
    
    return energy(moons, vels)

def gcd(a, b): return gcd(b, a % b) if b else a

def lcm(a, b): return a*b//gcd(a,b)

def loop(coord, moons, vels):
    seen = set()
    state = (moons[0][coord],moons[1][coord], moons[2][coord], moons[3][coord], vels[0][coord],vels[1][coord], vels[2][coord], vels[3][coord]) 
    cnt =0
    while state not in seen:
        seen.add(state)
        cnt += 1
        vels = grav(moons, vels, coord)
        moons = vel(moons, vels, coord)
        state = (moons[0][coord],moons[1][coord], moons[2][coord], moons[3][coord], vels[0][coord],vels[1][coord], vels[2][coord], vels[3][coord]) 
    return cnt
        


def p2(v, log=False):
    lines = v.strip().split('\n')
    moons = []
    for line in lines:
        x,y, z = map(int, re.sub("[^0-9- ]", "", line).split())
        moons.append([x, y, z])
    vels = [[0] * 3 for _ in range(4)]
    loops = []
    for coord in range(3):
        l= loop(coord, moons, vels)
        pp(l)
        loops.append(l)
    pp(loops)
    c = loops[0]
    for l in loops[1:]:
        c = lcm(c, l)
    pp(c)
        #apply vel

    return c

def pp(*v):
    if PP:
        print(v) 

def get_day():
    return 12

def get_year():
    return 2019



if __name__ == '__main__':
    #0 samples_only, 1 run everything, 2 only my input data
    DB = 2
    #Debugprint: print if 1, not if 0
    PP = 0
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
