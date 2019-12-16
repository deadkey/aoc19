import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
from collections import defaultdict as dd

def topsort(g):
    ps= dd(int)
    for ns in g:
        for n in g[ns]:
            ps[n] += 1
    q =['FUEL']
    order = []
    while q:
        q2 = []
        for n in q:
            order.append(n)
            for p in g[n]:
                ps[p] -=1
                if ps[p] == 0:
                    q2.append(p)
        q =q2
    return order

def bs(reactions, order, no_fuel):
      
    fuel = 'FUEL'
    ore = 'ORE'
    no_ore = 0
    req = dd(int)
    req[fuel] = no_fuel

    for el in order:
        no_req = req[el]
        #print(el, reactions[el])
        if el != ore:
            repl_no, repl_li = reactions[el]

            for no, rel in repl_li:
                req[rel] += (no_req + repl_no -1) //repl_no * no
        
    return req[ore]

def get_reactions(v):
    lines = v.strip().split('\n')
    reactions = dd(list)
    g= dd(list)
    for line in lines:
        left, right = line.split('=>')
        if len(right.split(','))>1:
            print('WARNING')
        elems = left.split(',')
        data_r = right.split()
        no_r, t_r = int(data_r[0]), data_r[-1]
        
        needed = []
        for el in elems:
            data = el.split()
            no= int(data[0])
            t = data[-1]
            needed.append((no, t))
            g[t_r].append(t)
        reactions[t_r] =(no_r, needed)
    order = topsort(g)
    return reactions, order


def p1(v, log=False):
    lines = v.strip().split('\n')
    reactions = dd(list)
    g= dd(list)
    for line in lines:
        left, right = line.split('=>')
        if len(right.split(','))>1:
            print('WARNING')
        elems = left.split(',')
        data_r = right.split()
        no_r, t_r = int(data_r[0]), data_r[-1]
        
        needed = []
        for el in elems:
            data = el.split()
            no= int(data[0])
            t = data[-1]
            needed.append((no, t))
            g[t_r].append(t)
        reactions[t_r] =(no_r, needed)
    order = topsort(g)
    
    fuel = 'FUEL'
    ore = 'ORE'
    no_ore = 0
    req = dd(int)
    req[fuel] = 1

    for el in order:
        no_req = req[el]
        #print(el, reactions[el])
        if el != ore:
            repl_no, repl_li = reactions[el]

            for no, rel in repl_li:
                req[rel] += (no_req + repl_no -1) //repl_no * no
        
    return req[ore]

def p2(v, log=False):
    reactions, order = get_reactions(v)
    lo, hi = 0, 1000000000000
    N = 1000000000000
    for i in range(50):
        mid = (lo + hi)//2
        ore = bs(reactions, order, mid)
        print(ore)
        if ore > N:
            hi = mid
        else:
            lo = mid
        
    return lo

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
    PP = 0
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
