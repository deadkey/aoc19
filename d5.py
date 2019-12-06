import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

def p1(v, log=False):
    return 0
    '''
    output = -1
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
            v1 = int(cmd[i+1])
            
        if code == 6:
            v1 = int(cmd[i+1])

        if code == 7:
            v1 = int(cmd[i+1])

        if code == 8:
            v1 = int(cmd[i+1])
            

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

            cmd[pos] = 1
            i += 2

            #print('ins', i, cmd, pos)

        elif code == 4:
            pos = v1
            output = cmd[pos]
            i += 2

            print('out', output)
        elif code == 5:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            
            pos = b
            if a != 0:
                i = b
            else:
                i += 2

        elif code == 6:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            b = v2
            if p2 == 0:
                b = cmd[v2]
            
            pos = b
            if a == 0:
                i = b
            else:
                i += 2
            
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
            i += 4
            
        elif code == 99:
            return output

        else:
            print('something went wrong', code, i)
            exit()
    '''
        
    return output

def p2(v, log=False):
    output = -1
    myin = 5
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

            cmd[pos] = myin

            #print('ins', i, cmd, pos)
            i += 2


        elif code == 4:
            a = v1
            if p1 == 0:
                a = cmd[v1]
            
            #print('output ', cmd, a, len(cmd))
            output = a
            i += 2

            print('out', output)

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
            return output

        else:
            print('something went wrong', i)
            exit()

        
    return output

def get_day():
    return date.today().day

def get_year():
    return date.today().year

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2, run_samples = False)
    #run(get_year(), get_day(), p1, p2, samples_only = True)
