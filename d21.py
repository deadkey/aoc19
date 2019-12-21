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

def p1(v, log=False):
    global offset
    offset = 0
    cmd= get_cmd(v)
    ins = Queue()
    cmds= """NOT A J
    NOT B T
    OR T J
    NOT C T
    OR T J
    AND D J
    WALK
    """ 
    for ch in cmds:
        ins.put(ord(ch))
    out = program(cmd, ins)
    ch_out = [chr(i) for i in out[0:-1]]
    s = ''.join(ch_out) + '\n'
    
    print(s)
    return out[-1]


def p2(v, log=False):
    global offset
    offset = 0
    cmd= get_cmd(v)
    ins = Queue()
    cmds= """NOT A J
    NOT B T
    OR T J
    NOT C T
    OR T J
    AND D J
    AND H J
    NOT A T
    OR T J
    RUN
    """ 
    
    for ch in cmds:
        ins.put(ord(ch))
    out = program(cmd, ins)
    ch_out = [chr(i) for i in out[0:-1]]
    s = ''.join(ch_out) + '\n'
    
    print(s)
    return out[-1]


def pp(*v):
    if PP:
        print(v) 

def get_day():
    return 21

def get_year():
    return 2019



if __name__ == '__main__':
    #0 samples_only, 1 run everything, 2 only my input data
    DB = 2
    #Debugprint: print if 1, not if 0
    PP = 1
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
