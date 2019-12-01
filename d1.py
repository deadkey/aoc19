import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

def p1(v, log=False):
    lines = v.strip().split('\n')
    su = 0
    for line in lines:
        n = int(line)
        su += (n//3) -2
    return su


def fuel(n):
    s = 0
    f = (n//3) -2
    while f > 0:
        s+= f
        f = (f//3) -2
    return s

def p2(v, log=False):
    lines = v.strip().split('\n')
    su = 0
    for line in lines:
        n = int(line)
        su += fuel(n)
    return su

def get_day():
    return 1

def get_year():
    return 2019

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
