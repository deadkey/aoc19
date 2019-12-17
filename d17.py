import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

from queue import Queue

def get_cmd(v):
    lines = v.strip().split('\n')
    cmd = defaultdict(int)
    i = 0
    for line in lines:
        no = line.strip().split(',')
        for n in no:

            if len(n) > 0:
                cmd[i] = int(n)
                i += 1

    return cmd

offset = 0

def get(i, p, v, cmd):
    global offset
    if p[i] == 2:
        mem = offset + v[i]
        return cmd[mem]
    if p[i] == 0:
        return cmd[v[i]]
    
    return v[i]


def program(cmd, ins):
    global offset
    output = []

    i = 0
    while True:
        opcode = str(cmd[i])[::-1] + '0' * 6
        code = int(opcode[:2][::-1]) # note reversed!
        p = [int(opcode[2]), int(opcode[3]), int(opcode[4]), int(opcode[5])]
        N = len(cmd)
        v = [cmd[(i+1)%N], cmd[(i+2)%N], cmd[(i+3)%N], cmd[(i+4)%N]]
        
        a = get(0, p, v, cmd)
        b = get(1, p, v, cmd)

        pos = v[2]
        if p[2] == 2:
            pos += offset
        #ADD
        if code == 1:
            
            cmd[pos] = a + b
            i += 4
            
        #MUL
        elif code == 2:

            cmd[pos] = a * b
            i += 4

        #INPUT
        elif code == 3:
            
            #DIFFERENT POS!
            pos = v[0]
            if p[0] == 2:
                pos = v[0] + offset
            cmd[pos] = ins.get()
            
                
            i += 2

        #OUTPUT
        elif code == 4:

            output.append(a)
            i += 2

        
        #JUMP IF NOT ZERO
        elif code == 5:
            if a != 0:
                i = b
            else:
                i += 3
            
            
        #JUMP IF ZERO
        elif code == 6:
            if a == 0:
                i = b

            else:

                i += 3
        #LESS     
        elif code == 7:
            if a < b:
                cmd[pos] = 1
            else:
                cmd[pos] = 0
            i += 4


        #EQ
        elif code == 8:
            if a == b:
                cmd[pos] = 1
            else:
                cmd[pos] = 0
            
            i += 4
        #Changing offset
        elif code == 9:
            offset += a
            i += 2

        #DONE!
        elif code == 99:
            return output

        else:
            print('something went wrong', i)
            exit()

        
    return output

def create_map(v):
    def intersect(r, c):
        return (grid[r][c] == '#' and 
            grid[r-1][c] == '#' and
            grid[r+1][c] == '#' and
            grid[r][c-1] == '#' and
            grid[r][c+1] == '#')
    global offset
    offset = 0
    cmd= get_cmd(v)
    ins = Queue()
    output = program(cmd, ins)
    out_s = []
    for a in output:
        ch = chr(a)
        out_s.append(ch)
    s = ''.join(out_s)
    grid = []
    for line in s.split('\n'):
        L = line.strip()
        if len(L) > 0:
            grid.append(list(L))
    return grid


def p1(v, log=False):
    
    def intersect(r, c):
        return (grid[r][c] == '#' and 
            grid[r-1][c] == '#' and
            grid[r+1][c] == '#' and
            grid[r][c-1] == '#' and
            grid[r][c+1] == '#')
    global offset
    offset = 0
    cmd= get_cmd(v)
    ins = Queue()
    output = program(cmd, ins)
    out_s = []
    for a in output:
        ch = chr(a)
        out_s.append(ch)
    s = ''.join(out_s)
    grid = []
    for line in s.split('\n'):
        L = line.strip()
        if len(L) > 0:
            grid.append(list(L))
    print(s)
    cnt = 0
    for r in range(1, len(grid)-1):
        for c in range(1, len(grid[0])-1):
            if intersect(r, c):
                cnt += r * c

    return cnt

def p2(v, log=False):
    global offset
    offset = 0
    cmd= get_cmd(v)
    ins = Queue()
    cmd[0] = 2
    
    A = 'R,12,L,8,L,4,L,4'
    B = 'L,8,R,6,L,6'
    C = 'L,8,L,4,R,12,L,6,L,4'
    prog = 'A,B,A,B,C,A,C,A,C,B'
    s = prog + '\n' + A + '\n' + B + '\n' + C +'\n'
    for ch in s:
        ins.put(ord(ch))
    ins.put(ord('n'))
    ins.put(10)

    output = program(cmd, ins)
    
    return output[-1]

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
