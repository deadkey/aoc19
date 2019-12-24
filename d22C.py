import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

NEW_STACK = 'deal into new stack'
CUT = 'cut'
INC = 'deal with increment'

# returns g = gcd(a, b), x0, y0, 
# where g = x0*a + y0*b
def xgcd(a, b):
  x0, x1, y0, y1 = 1, 0, 0, 1
  while b != 0:
    q, a, b = (a // b, b, a % b)
    x0, x1 = (x1, x0 - q * x1)
    y0, y1 = (y1, y0 - q * y1)
  return (a, x0, y0)

def inv_inc(p, inc, MOD):
    return (p * xgcd(inc,MOD)[1]) % MOD

def inv_stack(p, L):
    return L - p -1

def inv_cut(c, p, L):
    return (p + c) % L


def cut(stack, no):
    if no < 0:
        #cut in the end
        c = stack[no:]
        rest = stack[0:no]
        return c + rest
    c = stack[0:no]
    rest = stack[no:]
    return rest + c

def inc(stack, no):
    new_stack = [0] * len(stack)
    i = 0
    for v in stack:
        new_stack[i] = v
        i += no
        i %= len(stack)
    return new_stack

def p1(v, log=False):
    return 0
    N = 10007 #change this!
    stack = [i for i in range(N)]
    lines = v.strip().split('\n')
    for line in lines:
        line = line.strip()
        if line == NEW_STACK:
            stack = stack[::-1]
        elif line.startswith(CUT):
            no = int(line.split()[-1])
            stack= cut(stack, no)
        elif line.startswith(INC):
            no = int(line.split()[-1])
            stack = inc(stack, no)
    
    #print(' '.join(map(str, stack)))
    for i, v in enumerate(stack):
        if v == 2019:
            return i

#0 1 2 3 4 5 6 7 8 9
#7 8 9 0 1 2 3 4 5 6  
def p2_2(v, log=False):
    N = 10
    T = 1
    lines = v.strip().split('\n')
    pos = 0
    for line in lines[::-1]:
        line = line.strip()
        if line == NEW_STACK:
            pos = inv_stack(pos, N)
            
        elif line.startswith(CUT):
            no = int(line.split()[-1])
            pos = inv_cut(no, pos, N)
        elif line.startswith(INC):
            no = int(line.split()[-1])
            pos = inv_inc(pos, no, N)
    
    return pos

def test(k, m, MOD, v, T):
    for i in range(T):
        v = (v * k + m) % MOD
    return v

def apply2(k, m, MOD):
    #((k * p + m) * k + m) % MOD
    # (k ** 2 * p + (k +1) * m) % MOD
    return k ** 2 % MOD, (k + 1) * m % MOD

def p2(v, log=False):
    T = 101741582076661
    #T = 10
    N = 119315717514047
    MOD = N
    #For 1
    k, m = -44404563805808, 89398771567475
    power = 0
    v = 2020
    #res = test(k, m, MOD, v, T)

    while 2 ** power <= T:
        if (2 ** power) & T:
            v = (k * v + m) % MOD
        k, m = apply2(k, m, MOD)
        power += 1
    #print(res, v)
    return v

def pp(*v):
    if PP:
        print(v) 

def get_day():
    return 22

def get_year():
    return 2019



if __name__ == '__main__':
    #0 samples_only, 1 run everything, 2 only my input data
    DB = 2
    #Debugprint: print if 1, not if 0
    PP = 1
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
