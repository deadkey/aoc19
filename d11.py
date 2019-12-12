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


def program(cmd, ins, i):
    global offset
    output = []

    
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
            cmd[pos] = ins.get()
            
            pp('ins', pos)
                
            i += 2

        #OUTPUT
        elif code == 4:

            output.append(a)
            i += 2

            if len(output) == 2:
                print('Cmd ', i)
                return cmd, output, i, False

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
        #Changing offset
        elif code == 9:
            offset += a
            pp('offset', offset)
            i += 2

        #DONE!
        elif code == 99:
             return cmd, output, i, True

        else:
            print('something went wrong', i)
            exit()


    return [], [], 0, True




def p1(v, log=False):
    return
    global offset
    offset = 0
    cmd= get_cmd(v)
    ins = Queue()
    ins.put(0)
    panels = dd(int)
    d = (-1, 0)
    pos = (0, 0)
    changeLeft = {(-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0)}
    changeRight = {(0, -1): (-1, 0), (1, 0): (0, -1), (0, 1):(1, 0), (-1, 0): (0, 1)}
    fin = False
    i = 0
    while not fin:
        res = program(cmd, ins, i)
        cmd, output, i, fin = res
        if fin:
            break
        color = output[0]
        change = output[1]
        panels[pos] = color
        if change == 0:
            d = changeLeft[d]
        elif change == 1:
            d = changeRight[d]
        pos = pos[0] + d[0], pos[1] + d[1]
        ins.put(panels[pos])
        
        pp('Drawing ', pos, 'new dir', d, 'output ', output, 'new input ', panels[pos])
    return len(panels)

def p2(v, log=False):
    global offset
    offset = 0
    cmd= get_cmd(v)
    ins = Queue()
    ins.put(1)
    panels = dd(int)
    d = (-1, 0)
    pos = (0, 0)
    changeLeft = {(-1, 0): (0, -1), (0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0)}
    changeRight = {(0, -1): (-1, 0), (1, 0): (0, -1), (0, 1):(1, 0), (-1, 0): (0, 1)}
    fin = False
    i = 0
    mnX, mnY, mxX, mxY = 0, 0, 0, 0
    while not fin:
        res = program(cmd, ins, i)
        cmd, output, i, fin = res
        if fin:
            break
        color = output[0]
        change = output[1]
        panels[pos] = color
        if change == 0:
            d = changeLeft[d]
        elif change == 1:
            d = changeRight[d]
        pos = pos[0] + d[0], pos[1] + d[1]
        ins.put(panels[pos])
        mnX = min(pos[0], mnX)
        mxX = max(pos[0], mxX)
        mnY = min(pos[1], mnY)
        mxY = max(pos[1], mxY)
             
    offX = mnX
    offY = mnY
    for r in range(mnX, mxX + 1):
        out = []
        for c in range(mnY, mxY + 1):
            color = panels[r, c]
            out.append('.' if color == 0 else 'X')
        print(''.join(out))


    return 0

def pp(*v):
    if PP:
        print(v) 

def get_day():
    return 11

def get_year():
    return 2019



if __name__ == '__main__':
    #0 samples_only, 1 run everything, 2 only my input data
    DB = 2
    #Debugprint: print if 1, not if 0
    PP = 1
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
