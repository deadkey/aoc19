import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

def p1(v, log=False):

    lines = v.strip().split('\n')
    cmd = []
    for line in lines:
        no = line.strip().split(',')
        for n in no:
            cmd.append(int(n))
    i = 0
    if len(cmd) > 20:
        cmd[1], cmd[2] = 12, 2
        #exit()
    
    while True:
        if cmd[i] == 1:
            a= cmd[cmd[i+1]]
            b = cmd[cmd[i+2]]
            pos = cmd[i+3]
            cmd[pos] = a + b
            #print('add', i, cmd, a+b)
        elif cmd[i] == 2:
            a= cmd[cmd[i+1]]
            b = cmd[cmd[i+2]]
            pos = cmd[i+3]
            cmd[pos] = a * b

            #print('mul', i, cmd, a*b)
        elif cmd[i] == 99:
            return cmd[0]
        else:
            print('something went wrong', i)
            exit()

        i += 4

def test(v, A, B):

    lines = v.strip().split('\n')
    cmd = []
    for line in lines:
        no = line.strip().split(',')
        for n in no:
            cmd.append(int(n))
    i = 0
    if len(cmd) > 20:
        cmd[1], cmd[2] = A, B
        #exit()
    
    while True:
        if cmd[i] == 1:
            a= cmd[cmd[i+1]]
            b = cmd[cmd[i+2]]
            pos = cmd[i+3]
            cmd[pos] = a + b
            #print('add', i, cmd, a+b)
        elif cmd[i] == 2:
            a= cmd[cmd[i+1]]
            b = cmd[cmd[i+2]]
            pos = cmd[i+3]
            cmd[pos] = a * b

            #print('mul', i, cmd, a*b)
        elif cmd[i] == 99:
            return cmd[0]
        else:
            print('something went wrong', i)
            exit()

        i += 4


def p2(v, log=False):
    D = 19690720
    for a in range(100):
        for b in range(100):
            res = test(v, a, b)
            
            if res == D:
                
                return 100 * a + b
    return 0

def get_day():
    return 2

def get_year():
    return 2019

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2, samples_only = False)
