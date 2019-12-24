import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
import time
try: 
    from queue import Queue
except:
    from Queue import Queue

from threading import Thread

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


def get(i, p, v, cmd, offset):
    if p[i] == 2:
        mem = offset + v[i]
        return cmd[mem]
    if p[i] == 0:
        return cmd[v[i]]
    
    return v[i]

def nat_th(all_ins, nat):
    x, y = -1, -1
    sent2zero = []
    Thread.sleep(10)
    new_data = False
    while True:
        Thread.sleep(1)
        cnt = 0
        for i in range(50):
            if all_ins[i].empty():
                cnt += 1

        data = nat.get()
        cmd, v = data
        if cmd== 'data':
            x, y = v
            pp('Got data', v)
            new_data = True

        if cnt == 50 and new_data:
            sent2zero.append((x, y))
            all_ins[0].put(x)
            all_ins[0].put(y)
            new_data = False
            if len(sent2zero) >= 2 and sent2zero[-2][1] == sent2zero[-1][1]:
                print('TWICE', y)
                exit() # Right answer 16424

    
    

def program(cmd, ins, all_ins, nat, index):
    output = []
    offset = 0
    read= []
    first = True
    hasRead = 0
    i = 0
    idleCnt = 0
    while True:
        opcode = str(cmd[i])[::-1] + '0' * 6
        code = int(opcode[:2][::-1]) # note reversed!
        p = [int(opcode[2]), int(opcode[3]), int(opcode[4]), int(opcode[5])]
        N = len(cmd)
        v = [cmd[(i+1)%N], cmd[(i+2)%N], cmd[(i+3)%N], cmd[(i+4)%N]]
        
        a = get(0, p, v, cmd, offset)
        b = get(1, p, v, cmd, offset)

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
            val = -1
            try:
                read.append(ins.get(timeout = 0.01))
                
                nat.put(('active', index))
                
            except:
                idleCnt += 1
                if idleCnt == 10:
                    nat.put(('idle', index))
                    idleCnt = 0
                
            
            if first:
                val = read[0]
                first = False
                read = read[1:]
                nat.put(('active', index))

            if len(read) >= 2:
                val = read[hasRead]
                hasRead += 1

                nat.put(('active', index))
                #pp('Read', read[0], read[1])
                if hasRead == 2:
                    read = read[2:]
                    hasRead = 0
            
            cmd[pos] = val
                
            i += 2

        #OUTPUT
        elif code == 4:

            output.append(a)
            i += 2
            idle = False  
            if len(output) == 3:
                addr = output[0]
                x = output[1]
                y = output[2]
                if addr != 255:
                    all_ins[addr].put(x)
                    all_ins[addr].put(y)
                    #pp('Send to {} {} {}'.format(addr, x, y))
                    nat.put(('active', index))
                    nat.put(('active', addr))
                else:
                    nat.put(('active', index))    
                    nat.put(('data', (x, y)))
                output =[]    
        
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
    return 0
    cmds=[get_cmd(v) for _ in range(50)]
    all_ins = [Queue() for i in range(50)]
    for i in range(50):
        all_ins[i].put(i)
    threads = []
    for i in range(50):
        thr = Thread(target = program, args = (cmds[i], all_ins[i], all_ins))
        threads.append(thr)
    pp('All created, start')
    for i in range(50):
        threads[i].start()
    for i in range(50):
        threads[i].join()
    return 0
    

def p2(v, log=False):
    cmds=[get_cmd(v) for _ in range(50)]
    all_ins = [Queue() for i in range(50)]
    nat = Queue()

    for i in range(50):
        all_ins[i].put(i)
    threads = []
    for i in range(50):
        thr = Thread(target = program, args = (cmds[i], all_ins[i], all_ins, nat, i))
        threads.append(thr)
    pp('All created, start')
    for i in range(50):
        threads[i].start()
    

    idle = set()
    x, y = -1, -1
    sent2zero = []
    new_data = False
    while True:
        data = nat.get()
        cmd, v = data
        if cmd== 'data':
            x, y = v
            pp('Got data', v)
            new_data = True

            
        elif cmd== 'idle':
            idle.add(v)

            #pp('Got idle', v)
        elif cmd == 'active' and v in idle:
            idle.remove(v)
            #pp('Got active')
        if len(idle) == 50 and new_data:
            sent2zero.append((x, y))
            all_ins[0].put(x)
            all_ins[0].put(y)
            new_data = False
            if len(sent2zero) >= 2 and sent2zero[-2][1] == sent2zero[-1][1]:
                print('TWICE', y)
                exit() # Right answer 16424

    
    for i in range(50):
        threads[i].join()
    
    
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
    PP = 1
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
