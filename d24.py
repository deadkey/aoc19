import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run

def get_day(): return date.today().day
def get_year(): return date.today().year

def p1(v, log=False):
    lines = v.strip().split('\n')
    return 0

def p2(v, log=False):
    lines = v.strip().split('\n')
    
    return 0

def pp(*v):
    if PP:
        print(v) 




if __name__ == '__main__':
    #0 samples_only, 1 run everything, 2 only my input data
    DB = 1
    #Debugprint: print if 1, not if 0
    PP = 0
    run(get_year(), get_day(), p1, p2, run_samples = DB < 2, samples_only = DB == 0)
