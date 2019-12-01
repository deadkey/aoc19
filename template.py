import sys, time
sys.path.extend(['..', '.'])
from collections import *
from main import run

def p1(v, log=False):
    return 0

def p2(v, log=False):
    return 0

def get_day():
    return date.today().day

def get_year():
    return date.today().year

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2, D=True)
