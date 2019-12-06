import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
from collections import defaultdict as dd
def d():
    return -1

def bfs(q, g):
    N = len(g)
    visited = dd(d)
    for node in q:
        visited[node] = 0
    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if visited[ne] == -1:
                    visited[ne] = visited[node] + 1
                    q2.append(ne)
        q = q2
    return visited

def bfs2(q, g, T):
    N = len(g)
    visited = dd(d)
    for node in q:
        visited[node] = 0
    while q:
        q2 = []
        for node in q:
            for ne in g[node]:
                if visited[ne] == -1:
                    visited[ne] = visited[node] + 1
                    q2.append(ne)
                
        q = q2
    return visited[T]

def p1(v, log=False):
    lines = v.strip().split('\n')
    g = dd(list)
    for line in lines:
        a, b = line.strip().split(')')
        g[a].append(b)
    
    orbits = bfs(['COM'], g)
    cnt = 0
    for n in g.keys():
        cnt += orbits[n]


    return cnt

def p2(v, log=False):
    lines = v.strip().split('\n')
    g = dd(list)
    your = ''
    santas = ''
    for line in lines:
        a, b = line.strip().split(')')
        g[a].append(b)
        g[b].append(a)
        if b == 'YOU':
            your = a
        if b == 'SAN':
            santas = a
    
    dist = bfs2([your], g, santas)
    
    return dist

def get_day():
    return date.today().day

def get_year():
    return date.today().year

if __name__ == '__main__':
    run(get_year(), get_day(), p1, p2)
