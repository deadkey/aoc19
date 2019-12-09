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
    cmd = []
    for line in lines:
        no = line.strip().split(',')
        for n in no:

            if len(n) > 0:
                cmd.append(int(n))
    return cmd

"""

def program(cmd, phase, to_use):
    output = -1
    used = 0
    lines = v.strip().split('\n')
    cmd = []
    for line in lines:
        no = line.strip().split(',')
        for n in no:

            if len(n) > 0:
                cmd.append(int(n))
    
    i = 0
    while True:
        opcode = str(cmd[i])[::-1] + '0' * 6
        code = int(opcode[:2][::-1]) # note reversed!
        p1 = int(opcode[2])
        p2 = int(opcode[3])
        p3 = int(opcode[4])
        p4 = int(opcode[5])
        
        v1, v2, v3, v4 = 0, 0, 0, 0
        if code == 1:
            v1, v2, v3 = int(cmd[i+1]), int(cmd[i+2]), int(cmd[i+3])     

        if code == 2:
            v1, v2, v3 = int(cmd[i+1]), int(cmd[i+2]), int(cmd[i+3])

        if code == 3:
            v1 = int(cmd[i+1])
        
        if code == 4:
            v1 = int(cmd[i+1])


        if code == 5:
            v1, v2 = int(cmd[i+1]), int(cmd[i+2])
            
        if code == 6:
            v1, v2 = int(cmd[i+1]), int(cmd[i+2])

        if code == 7:
            v1, v2, v3 = int(cmd[i+1]), int(cmd[i+2]), int(cmd[i+3])


        if code == 8:
            v1, v2, v3 = int(cmd[i+1]), int(cmd[i+2]), int(cmd[i+3])

            

        if code == 1:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            
            pos = v3
            
            cmd[pos] = a + b
            i += 4
            #print('add', i, cmd, a+b)
        elif code == 2:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            pos = v3
            cmd[pos] = a * b

            #print('mul', i, cmd, a*b)
            i += 4
        elif code == 3:
            a = 1
            pos = v1

            cmd[pos] = phase[used]
            used += 1
                

            #print('ins', i, cmd, pos)
            i += 2


        elif code == 4:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            
            #print('output ', cmd, a, len(cmd))
            output = a
            i += 2
            if used == to_use:
                return output, False, cmd
            #print('out', output)

        elif code == 5:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            
            if a != 0:
                i = b

                #print('jum not ', i, cmd, b)
            else:

                #print('skip jump n z ', i, cmd, b)
                i += 3
            

        elif code == 6:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            #print('jump eq ', v2, cmd[v2])
            if p2 == 0:
                b = cmd[v2]
            
            if a == 0:
                i = b

                #print('jum eq ', i, cmd, b, len(cmd))
            else:

                #print('skip jump z', i, cmd, b)
                i += 3
            
        elif code == 7:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            
            pos = v3

            if a < b:
                cmd[pos] = 1
            else:
                cmd[pos] = 0
            i += 4

            #print('less ', i, cmd, a < b)
        
        elif code == 8:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            
            pos = v3

            if a == b:
                cmd[pos] = 1
            else:
                cmd[pos] = 0
            
            #print('eq ', cmd, v3, cmd[v3], a == b)
            i += 4


        elif code == 99:
            return output, True, cmd

        else:
            print('something went wrong', i)
            exit()

        
    return output, True, cmd

"""

e_out = - 10 ** 12

def program(cmd, ins, outputs, is_e = False):
    global e_out
    i = 0
    while True:
        opcode = str(cmd[i])[::-1] + '0' * 6
        code = int(opcode[:2][::-1]) # note reversed!
        p1 = int(opcode[2])
        p2 = int(opcode[3])
        p3 = int(opcode[4])
        p4 = int(opcode[5])
        
        v1, v2, v3, v4 = 0, 0, 0, 0
        if code == 1:
            v1, v2, v3 = int(cmd[i+1]), int(cmd[i+2]), int(cmd[i+3])     

        if code == 2:
            v1, v2, v3 = int(cmd[i+1]), int(cmd[i+2]), int(cmd[i+3])

        if code == 3:
            v1 = int(cmd[i+1])
        
        if code == 4:
            v1 = int(cmd[i+1])


        if code == 5:
            v1, v2 = int(cmd[i+1]), int(cmd[i+2])
            
        if code == 6:
            v1, v2 = int(cmd[i+1]), int(cmd[i+2])

        if code == 7:
            v1, v2, v3 = int(cmd[i+1]), int(cmd[i+2]), int(cmd[i+3])


        if code == 8:
            v1, v2, v3 = int(cmd[i+1]), int(cmd[i+2]), int(cmd[i+3])

            

        if code == 1:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            
            pos = v3
            
            cmd[pos] = a + b
            i += 4
            #print('add', i, cmd, a+b)
        elif code == 2:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            pos = v3
            cmd[pos] = a * b

            #print('mul', i, cmd, a*b)
            i += 4
        elif code == 3:
            a = 1
            pos = v1
            #READS INPUT
            
            cmd[pos] = ins.get()

            #print('ins', i, cmd, pos)
            i += 2


        elif code == 4:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            
            #print('output ', cmd, a, len(cmd))
            outputs.put(a)
            if is_e:
                print(a)
                e_out = a
            i += 2
            #print('out', output)

        elif code == 5:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            
            if a != 0:
                i = b

                #print('jum not ', i, cmd, b)
            else:

                #print('skip jump n z ', i, cmd, b)
                i += 3
            

        elif code == 6:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            #print('jump eq ', v2, cmd[v2])
            if p2 == 0:
                b = cmd[v2]
            
            if a == 0:
                i = b

                #print('jum eq ', i, cmd, b, len(cmd))
            else:

                #print('skip jump z', i, cmd, b)
                i += 3
            
        elif code == 7:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            
            pos = v3

            if a < b:
                cmd[pos] = 1
            else:
                cmd[pos] = 0
            i += 4

            #print('less ', i, cmd, a < b)
        
        elif code == 8:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            
            pos = v3

            if a == b:
                cmd[pos] = 1
            else:
                cmd[pos] = 0
            
            #print('eq ', cmd, v3, cmd[v3], a == b)
            i += 4


        elif code == 99:
            return True

        else:
            print('something went wrong', i)
            exit()

        
    return True

def test_phase(v, ph):
    a_out = program(v, [ph[0], 0], 2)
    b_out = program(v, [ph[1], a_out], 2)
    c_out = program(v, [ph[2], b_out], 2)
    d_out = program(v, [ph[3], c_out], 1)
    e_out = program(v, [ph[4], d_out], 1)
    return e_out
                     

def p1(v, log=False):
    return
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

    tsa = Thread(target = program, args = (cmds[0], ins[0],ins[1]))
    
    tsb = Thread(target = program, args = (cmds[1], ins[1],ins[2]))

    tsc = Thread(target = program, args = (cmds[2], ins[2],ins[3]))

    tsd = Thread(target = program, args = (cmds[3], ins[3],ins[4]))

    tse = Thread(target = program, args = (cmds[4], ins[4],ins[0], True))
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
    return 0
    ph= [5, 6, 7, 8, 9]
    perms= permutations(ph)
    mx_out = -10 ** 12
    for p  in perms:

        test_phase2(v, p)
        if e_out > mx_out:
            mx_out = e_out
            #print(p, mx_out)


    return mx_out
   

def get_day():
    return 7

def get_year():
    return 2019

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2, run_samples = False)
