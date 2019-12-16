import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

from queue import Queue
from collections import defaultdict as dd

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


def program3(cmd, ins, i):
    global offset
    output = []
    blocks = 0
    score = 0
    joy = 0, 0
    ball = 0, 0
    
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
            
            pp('add vals', p[0], v[0], p[1], v[1], p[2], v[2])
            cmd[pos] = a + b
            i += 4
            pp('add', a, b, pos)
            
        #MUL
        elif code == 2:

            pp('mul vals', p[0], v[0], p[1], v[1])
            cmd[pos] = a * b
            i += 4

            pp('mul', a, b, pos)
        #INPUT
        elif code == 3:
            
            #DIFFERENT POS!
            pos = v[0]
            if p[0] == 2:
                pos = v[0] + offset
            ddd = moveto(ball, joy)
            print('Moving', ball, joy, ddd)
            cmd[pos] = ddd
            
            pp('ins', pos)
                
            i += 2

        #OUTPUT
        elif code == 4:

            output.append(a)
            i += 2

            if len(output) == 3:
                x = output[0]
                y = output[1]
                t = output[2]
                output = []
                if (x, y) == (-1, 0):
                    score = t
                elif t == 3:
                    joy = x, y
                elif t == 4:
                    ball = x,y
                elif t == 2:
                    blocks += 1
                pp(x, y, t)
            

        
        #JUMP IF NOT ZERO
        elif code == 5:
            if a != 0:
                i = b
            else:
                i += 3
            
            pp('jmp', a, b)
            
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

            pp('less', a, b)

        #EQ
        elif code == 8:
            if a == b:
                cmd[pos] = 1
            else:
                cmd[pos] = 0
            
            i += 4
            pp('eq', a, b)
        #Changing offset
        elif code == 9:
            offset += a
            pp('offset', offset)
            i += 2

        #DONE!
        elif code == 99:
             return blocks, score

        else:
            print('something went wrong', i)
            exit()


    return [], [], 0, True

offset =0

def p1(v, log=False):
    global offset
    offset = 0
    return 0
    cmd= get_cmd(v)
    ins = Queue()
    i = 0
    blocks, score = program3(cmd, ins, i)
       
    return blocks
    
def printpanel():
    global  mnX, mnY, mxX, mxY
    types = ['.', 'X', '#', '_', 'o']
    for c in range(mnY, mxY + 1):
        out = []
        for r in range(mnX, mxX + 1):
            t = panels[r, c]
            out.append(types[t])
        print(''.join(out))
    print()

def moveto(ball, joy):
    dx = ball[0] -joy[0]
    #print('diff x', dx)
    if dx > 0:
        return 1
    if dx < 0:
        return -1
    return 0

def close(ball, joy):
    return joy[1] - ball[1] == 1 

def p2(v, log=False):

    offset = 0
    cmd= get_cmd(v)
    cmd[0] = 2
    ins = Queue()
    i = 0
    blocks, score = program3(cmd, ins, i)
       
    return score

def pp(*v):
    if PP:
        print(v) 

def get_day():
    return date.today().day

def get_year():
    return date.today().year



if __name__ == '__main__':
    #0 samples_only, 1 run everything, 2 only my input data
    DB = 1
    #Debugprint: print if 1, not if 0
    PP = 0
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
