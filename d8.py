import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run


def p1(v, log=False): 
    lines = v.strip().split('\n')
    digits = []
    for line in lines:
        for ch in line.strip():
            digits.append(int(ch))
    W = 25 #my input
    H = 6 #my input
    fewest = 10**12, 0
    
    for layer in range(0, len(digits), W * H):
        lay = digits[layer: layer+W*H]
        cnt = Counter(lay)
        fewest = min(fewest, (cnt[0], cnt[1] * cnt[2]))
        
    return fewest[1]

def p2(v, log=False):
    lines = v.strip().split('\n')
    digits = []
    for line in lines:
        for ch in line.strip():
            digits.append(int(ch))
    itr = iter(digits)
    W = 25 #my input
    H = 6 #my input
    
    seen = [[-1]  * W for _ in range(H)]
    k = len(digits) // (W * H)
    
    for layer in range(k):
        for row in range(H):
            for col in range(W):
                ch = next(itr)
                if seen[row][col] == -1 or seen[row][col] == 2:    
                    seen[row][col] = ch
                
                
    for row in range(H):
        out =[]
        for col in range(W):
            if seen[row][col] == 0:
                out.append('.')
            else:
                out.append('X')

        print(''.join(map(str, out)))
             
    return 0

def get_day():
    return 8

def get_year():
    return 2019

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2, run_samples = False)
