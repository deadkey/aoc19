import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
from collections import Counter

#1610 1104
def has2(n):
    no=list(str(n))
    s = set(str(n))
    return len(s) < len(no)

def has22(n):
    cnt = Counter(str(n))
    return 2 in cnt.values()
    

def inc(n):
    no = list(str(n))
    return no == sorted(no)
    


def p1(v, log=False):
    start, end = map(int, v.strip().split('-'))
    cnt= 0
    for n in range(start, end+1):
        if has2(n) and inc(n):
            cnt+= 1
    return cnt

def p2(v, log=False):
    start, end = map(int, v.strip().split('-'))
    cnt= 0
    for n in range(start, end+1):
        if has22(n) and inc(n):
            cnt+= 1
    return cnt
    

def get_day():
    return date.today().day

def get_year():
    return date.today().year

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2, D=True)
