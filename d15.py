import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
from queue import Queue

sys.setrecursionlimit(10000)

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
    output = -1


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

            i += 2
            return a, cmd, i
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
            return output, cmd, i

        else:
            print('something went wrong', i)
            exit()

        
    return output, cmd, i


def fill(seen, ox):
    visited = set()
    visited.add((0, 0))
    q= [(0, 0)]
    dists = {}
    dists[(0, 0)] = 0

    while q:
        q2 = []
        cand= [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r, c in q:
            for d in cand:
                ne = r + d[0], c + d[1]
                if ne in seen and seen[ne] == 0 or ne not in seen:
                    continue

                if ne not in visited:
                        visited.add(ne)
                        dists[ne] = dists[r, c] + 1
                        q2.append(ne)
        q = q2
    return dists[ox]


def bfs(seen, ox):
    visited = set()
    visited.add((0, 0))
    q= [(0, 0)]
    dists = {}
    dists[(0, 0)] = 0

    while q:
        q2 = []
        cand= [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r, c in q:
            for d in cand:
                ne = r + d[0], c + d[1]
                if ne in seen and seen[ne] == 0 or ne not in seen:
                    continue

                if ne not in visited:
                        visited.add(ne)
                        dists[ne] = dists[r, c] + 1
                        q2.append(ne)
        q = q2
    return dists[ox]


def bfs2(seen, ox):
    visited = set()
    visited.add(ox)
    q= [ox]
    dists = {}
    dists[ox] = 0

    while q:
        q2 = []
        cand= [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r, c in q:
            for d in cand:
                ne = r + d[0], c + d[1]
                if ne in seen and seen[ne] == 0 or ne not in seen:
                    continue

                if ne not in visited:
                        visited.add(ne)
                        dists[ne] = dists[r, c] + 1
                        q2.append(ne)
        q = q2
    return max(dists.values())

def dfs(cmd, ins, i, curr, seen, path):
    dirs = {1:(-1, 0), 2: (1, 0),3:(0, -1), 4:(0, 1)}
    back = {1: 2, 2:1, 3:4, 4:3}
    
    for d in dirs:
        dr, dc = dirs[d]
        nr, nc = path[-1][0] + dr, path[-1][1] + dc

        if (nr, nc) not in seen:
            ins.put(d)
            out, cmd, i = program(cmd, ins, i)
            seen[nr,nc] = out
            if out == 2:
                return nr, nc 
                
            
            if out == 1:
                path.append((nr, nc))
                oxpos = dfs(cmd, ins, i, (nr, nc), seen, path)
                if oxpos != (-1, -1):
                    return oxpos
                path.pop()
                back_dir = back[d]
                ins.put(back_dir)
                out, cmd, i = program(cmd, ins, i)
        
    return -1, -1
        

def dfs2(cmd, ins, i, curr, seen, path):
    
    dirs = {1:(-1, 0), 2: (1, 0),3:(0, -1), 4:(0, 1)}
    back = {1: 2, 2:1, 3:4, 4:3}
    oxpos = None
    for d in dirs:
        dr, dc = dirs[d]
        nr, nc = path[-1][0] + dr, path[-1][1] + dc

        if (nr, nc) not in seen:
            ins.put(d)
            #print('Walking in ', d)
            out, cmd, i = program(cmd, ins, i)
            #print('Got ', out)
            seen[nr,nc] = out
            if out == 2:
                oxpos= nr, nc 
                
            
            if out != 0:
                path.append((nr, nc))
                alt = dfs2(cmd, ins, i, (nr, nc), seen, path)
                if alt != None:
                    oxpos = alt
                path.pop()
                back_dir = back[d]
                ins.put(back_dir)
                out, cmd, i = program(cmd, ins, i)
    
    return oxpos
    
            

def p1(v, log=False):
    global offset, i
    offset = 0
    i =0
    cmd= get_cmd(v)
    ins = Queue()
    wall, empty, ox = 0, 1, 2
    curr = 0, 0
    seen = {}
   
    i = 0
    path = [(0, 0)]
    oxpos = dfs(cmd, ins, i, curr, seen, path)
    return bfs(seen, oxpos)

def p2(v, log=False):
    global offset, i
    offset = 0
    i =0
    cmd= get_cmd(v)
    ins = Queue()
    wall, empty, ox = 0, 1, 2
    curr = 0, 0
    seen = {}
    i = 0
    path = [(0, 0)]
    oxpos = dfs2(cmd, ins, i, curr, seen, path)
    return bfs2(seen, oxpos)

def pp(*v):
    if PP:
        print(v) 

def get_day():
    return 15

def get_year():
    return 2019



if __name__ == '__main__':
    #0 samples_only, 1 run everything, 2 only my input data
    DB = 1
    #Debugprint: print if 1, not if 0
    PP = 0
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
