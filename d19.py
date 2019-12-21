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

'''
def get(i, p, v, cmd):
    global offset
    if p[i] == 2:
        mem = offset + v[i]
        return cmd[mem]
    if p[i] == 0:
        return cmd[v[i]]
    
    return v[i]
'''

def get(v, digs):
    s = str(digs[v])
    s = '0'*(5 - len(s)) + s
    op = digs[v]%100
    p1 = int(s[-3])
    p2 = int(s[-4])
    p3 = int(s[-5])
    return p3, p2, p1, op

def getV(v, mode, digs, rb):
    if mode == 1: return v
    elif mode == 0: return digs[v]
    else: return digs[v+rb]

def run_prog(digs, q_in, q_out):
    
    L = len(digs)
    
    i = 0
    rb = 0
    last_out = None
    inc = [None, 4, 4, 2, 2, 3, 3, 4, 4, 2]
    while i < L:
        C, B, A, op = get(i, digs)
        if op == 99: break
        elif op == 1:
            a, b, c = digs[i+1], digs[i+2], digs[i+3]
            digs[c + (rb if C==2 else 0)] = getV(a, A, digs, rb) + getV(b, B, digs, rb)
        elif op == 2:
            a, b, c = digs[i+1], digs[i+2], digs[i+3]
            digs[c+ (rb if C==2 else 0)] = getV(a, A, digs, rb) * getV(b, B, digs, rb)
        elif op == 3:
            a = digs[i+1]
            digs[a+ (rb if A==2 else 0)] = q_in.get()
        elif op == 4:
            a = digs[i+1]
            o = getV(a, A, digs, rb)
            q_out.append(o)
            last_out = o
        elif op == 5:
            a, b = digs[i+1], digs[i+2]
            if getV(a, A, digs, rb):
                i = getV(b, B, digs, rb)
                continue
        elif op == 6:
            a, b = digs[i+1], digs[i+2]
            if getV(a, A, digs, rb) == 0:
                i = getV(b, B, digs, rb)
                continue
        elif op == 7:
            a, b, c = digs[i+1], digs[i+2], digs[i+3]
            VAL = int(getV(a, A, digs, rb) < getV(b, B, digs, rb))
            digs[c+ (rb if C==2 else 0)] = VAL
        elif op == 8:
            a, b, c = digs[i+1], digs[i+2], digs[i+3]
            VAL = int(getV(a, A, digs, rb) == getV(b, B, digs, rb))
            digs[c+ (rb if C==2 else 0)] = VAL
        elif op == 9:
            a = digs[i+1]
            rb += getV(a, A, digs, rb)

        else:
            print('wtf, op: {} ip: {}'.format(op, i))
            return
        i += inc[op]
    return last_out


def p1(v, log=False):
    global offset
    offset = 0
    cmd= get_cmd(v)
    ins = Queue()
    out= []
    grid = [['.'] * 50 for _ in range(50)]
    ins.put(0)
    ins.put(0)
    print('Hej')

    run_prog(cmd, ins, out)
    print('Out 1', out)

    ins.put(0)
    ins.put(1)

    run_prog(cmd, ins, out)
    print('Out', out)


    ins.put(1)
    ins.put(1)

    run_prog(cmd, ins, out)
    print('Out', out)

    return 0
    for r in range(50):
        for c in range(50):
            
            run_prog(cmd, ins, out)
            print('Out', out)
           
    return 0

def p2(v, log=False):
    lines = v.strip().split('\n')
    
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
    DB = 1
    #Debugprint: print if 1, not if 0
    PP = 1
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
