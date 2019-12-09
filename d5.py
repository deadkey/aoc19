import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

from queue import Queue

## RUN WITH PYTHON 3!!!!

def p1(v, log=False):
    cmd= get_cmd(v)
    ins = Queue()
    ins.put(1)
    return program(cmd, ins)

def pp(*v):
    if PP:
        print(v) 

def get(i, p, v, cmd):
    if p[i] == 0:
        return cmd[v[i]]
    
    return v[i]

def program(cmd, ins):
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
            cmd[pos] = ins.get()
            
            pp('ins', pos)
                
            i += 2

        #OUTPUT
        elif code == 4:

            output.append(a)
            i += 2

            pp('out', output)
        
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
       
        #DONE!
        elif code == 99:
            return output

        else:
            print('something went wrong', i)
            exit()

        
    return output

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


def p2(v, log=False):
    cmd= get_cmd(v)
    ins = Queue()
    ins.put(5)
    return program(cmd, ins)

def get_day():
    return 5

def get_year():
    return 2019

if __name__ == '__main__':
    #0 samples_only, 1 run everything, 2 only my input data
    DB = 2
    #Debugprint: print if 1, not if 0
    PP = 0
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
