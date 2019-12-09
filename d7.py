import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
from itertools import permutations
from collections import deque
from queue import Queue
from threading import Thread

## RUN WITH PYTHON 3!!!!

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


def get(i, p, v, cmd):
    if p[i] == 0:
        return cmd[v[i]]
    
    return v[i]


def program(cmd, phase, to_use):
    output = -1
    used = 0
    
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
            a = 1
            #DIFFERENT POS!
            cmd[v[0]] = phase[used]
            used += 1
                
            i += 2

        #OUTPUT
        elif code == 4:

            output = a
            i += 2
            if used == to_use:
                return output
            pp('out', output)
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

        #DONE!
        elif code == 99:
            return output

        else:
            print('something went wrong', i)
            exit()

        
    return output



e_out = - 10 ** 12

def get(i, p, v, cmd):
    if p[i] == 0 and v[i] < len(cmd):
        return cmd[v[i]]
    return v[i]

def program2(cmd, ins, outputs, is_e = False):
    global e_out
   
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
            #READS INPUT
            #DIFFERENT POS!
            pos = v[0]

            cmd[pos] = ins.get()
            i += 2
        #OUTPUT
        elif code == 4:
            
            outputs.put(a)
            
            if is_e:
                #print(a)
                e_out = a
            i += 2
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
            return outputs

        else:
            print('something went wrong', i)
            exit()

        
    return True

def test_phase(v, ph):
    cmds= [get_cmd(v) for _ in range(5)]

    a_out = program(cmds[0], [ph[0], 0], 2)
    b_out = program(cmds[1], [ph[1], a_out], 2)
    c_out = program(cmds[2], [ph[2], b_out], 2)
    d_out = program(cmds[3], [ph[3], c_out], 1)
    e_out = program(cmds[4], [ph[4], d_out], 1)
    return e_out
                     

def p1(v, log=False):
    
    ph= [0, 1, 2, 3, 4]
    perms= permutations(ph)
    mx_out = -10 ** 12
    for p  in perms:

        e_out = test_phase(v, p)
        if e_out > mx_out:
            mx_out = e_out
            #print(p, mx_out)


    return mx_out



def test_phase2(v, ph):
    
    term= False
    cmds=[get_cmd(v) for _ in range(5)]
    ins = [Queue() for i in range(5)]
    for i in range(5):
        ins[i].put(ph[i])
    ins[0].put(0)

    tsa = Thread(target = program2, args = (cmds[0], ins[0],ins[1]))
    
    tsb = Thread(target = program2, args = (cmds[1], ins[1],ins[2]))

    tsc = Thread(target = program2, args = (cmds[2], ins[2],ins[3]))

    tsd = Thread(target = program2, args = (cmds[3], ins[3],ins[4]))

    tse = Thread(target = program2, args = (cmds[4], ins[4],ins[0], True))
    tsa.start()
    tsb.start()
    tsc.start()
    tsd.start()
    tse.start()
    
    tsa.join()
    tsb.join()
    tsc.join()
    tsd.join()
    tse.join()
    
     

def p2(v, log=False):
    
    ph= [5, 6, 7, 8, 9]
    perms= permutations(ph)
    mx_out = -10 ** 12
    for p  in perms:

        test_phase2(v, p)
        if e_out > mx_out:
            mx_out = e_out
            #print(p, mx_out)

    return mx_out

def pp(*v):
    if PP:
        print(v) 

def get_day():
    return 7

def get_year():
    return 2019

if __name__ == '__main__':
    #0 samples_only, 1 run everything, 2 only my input data
    DB = 2
    PP = 0
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
