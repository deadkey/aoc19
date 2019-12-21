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
            pp('add', pos, a, i)
            
        #MUL
        elif code == 2:

            cmd[pos] = a * b
            i += 4

            pp('mul', pos, a, i)

        #INPUT
        elif code == 3:
            
            #DIFFERENT POS!
            pos = v[0]
            if p[0] == 2:
                pos = v[0] + offset
            cmd[pos] = ins.get()
            
            pp('in', pos, cmd[pos])
                
            i += 2

        #OUTPUT
        elif code == 4:

            output.append(a)
            i += 2
            pp('out', a,i)
        
        #JUMP IF NOT ZERO
        elif code == 5:
            if a != 0:
                i = b
            else:
                i += 3
            
            pp('jmp', pos, a, i)
            
        #JUMP IF ZERO
        elif code == 6:
            if a == 0:
                i = b

            else:

                i += 3
            
            pp('jmp 2', pos, a, i)
        #LESS     
        elif code == 7:
            if a < b:
                cmd[pos] = 1
            else:
                cmd[pos] = 0
            i += 4

            pp('less', pos, a, i)


        #EQ
        elif code == 8:
            if a == b:
                cmd[pos] = 1
            else:
                cmd[pos] = 0
            
            i += 4

            pp('eq', pos, a, i)
        #Changing offset
        elif code == 9:
            offset += a
            i += 2

            pp('offs', pos, a, i)

        #DONE!
        elif code == 99:
            pp('return')
            return output

        else:
            i += 1
            print('something went wrong', i)
            
            #return [0]
            

        
    return output



def p1(v, log=False):
    return 0
    global offset
    offset = 0
    cmd= get_cmd(v)
    ins = Queue()
    
    grid = [['.'] * 50 for _ in range(50)]
    cnt = 0
    for r in range(50):
        p = []
        for c in range(50):
            ins.put(r)
            ins.put(c)
            out = program(get_cmd(v), ins)
            for o in out:
                p.append(str(o))
                if o == 1:
                    cnt += 1
        print(''.join(p))
           
    return cnt

def p2(v, log=False):
    global offset
    offset = 0
    cmd= get_cmd(v)
    ins = Queue()
    
    grid = [['.'] * 50 for _ in range(50)]
    pos = set()

    lines = sys.stdin.readlines()
    grid = {}
    pos = set()
   
    for r, line in enumerate(lines):
        L = []
        for c, ch in enumerate(line.strip()):
            grid[r, c] = int(ch)
    
    cache = open('d19save4.txt', 'w+')
    

    for r in range(0, 1300):
        p = []
        for c in range(0, 1800):
            if (r, c) in grid:
                p.append(grid[r, c])
            else:
                ins.put(r)
                ins.put(c)
                out = program(get_cmd(v), ins)
                for o in out:
                    p.append(o)
                
        s =''.join(map(str, p))
        cache.write(s)
        cache.write('\n')
        print('Row', r)
    cache.close()
           
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
    PP = 0
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
