import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run


def pattern(inp, pos):
    su = 0
    pattern = [0] * (pos) + [1] * (pos+1) + [0] * (pos+1) + [-1] * (pos+1) 
    pattern2 = [0] * (pos+1) + [1] * (pos+1) + [0] * (pos+1) + [-1] * (pos+1)
    for i, v in enumerate(inp):
        mul = pattern2[(i - len(pattern))%len(pattern2)]
        if i < len(pattern):
            mul = pattern[i%len(pattern)]
        su += (v * mul)
    return abs(su)%10


def p1(v, log=False):
    return 0
    lines = v.strip().split('\n')
    inp =[int(ch) for ch in lines[0]]
    
    for ph in range(4):
        new_inp = []
        for i in range(len(inp)):
            new_v = pattern(inp, i)
            new_inp.append(new_v)
        inp = new_inp
        #print(inp)
            
    out = ''.join(map(str, inp[:8]))
    return out



def suffix_sum(inp):
    suffix = [0]
    su = 0
    for v in inp[::-1]:
        su += v
        suffix.append(su)
    return suffix[::-1]

def p2(v, log=False):
    lines = v.strip().split('\n')
    offset = int(lines[0][0:7])    
    inp =[int(ch) for ch in lines[0]]
    end = [inp[i%len(inp)] for i in range(offset, 10000 * len(inp))]

    for ph in range(100):
        su = 0
        for i in range(len(end) -1, -1, -1):
            su += end[i]
            su %= 10
            end[i] = su    
        
        #print(inp)
            
    out = ''.join(map(str, end[0:8]))
    return out


    return 0

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
