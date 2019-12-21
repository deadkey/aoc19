import sys, time
from datetime import date
sys.path.extend(['..', '.'])
from collections import *
from main import run
from collections import defaultdict as dd


def bfs2(start, goal, grid, iset, oset, inside, outside):
    visited = set()
    visited.add(start)
    q = [start]
    dist = {}
    dist[start] = 0

    while q:
        q2 = []

        dirs =[(-1, 0), (1, 0), (0, -1), (0, 1)]
        for pos, level in q:
            if (pos, level) == goal:
                return dist[goal]
            for dr, dc in dirs:
                ne = pos[0] + dr, pos[1] + dc
                if grid[ne[0]][ne[1]] != '.':
                    continue
                
                if (ne, level) in visited:
                    continue
                
                dist[(ne,level)] = dist[(pos, level)] +1
                visited.add((ne, level))
                q2.append((ne,level))

            if pos in iset:
                #go deeper
                label = iset[pos]
                outpos = outside[label]
                dist[(outpos, level +1)]= dist[(pos,level)] +1
                q2.append((outpos, level+1))
                visited.add((outpos, level+1))
                
            elif pos in oset and level > 0:
                #go up
                label = oset[pos]
                inpos = inside[label]
                dist[(inpos, level -1)]= dist[(pos,level)] +1
                q2.append((inpos, level-1))
                visited.add((inpos, level-1))
                
                    
                    
        q = q2
    return 10 ** 12 


def bfs(start, grid, poi):
    visited = set()
    
    visited.add(start)
    q = [start]
    dist = {}
    dist[start] = 0
    out = []

    while q:
        q2 = []

        dirs =[(-1, 0), (1, 0), (0, -1), (0, 1)]
        for r, c in q:
            
            for dr, dc in dirs:
                ne = r + dr, c + dc
                if grid[ne[0]][ne[1]] != '.':
                    continue

                if ne not in visited:
                    visited.add(ne)
                    

                    dist[ne]  = dist[r, c] + 1
                    if ne in poi:
                        out.append((dist[ne], (ne[0], ne[1])))
                    q2.append(ne)
        q = q2
    return out

def inf():
    return 10 ** 12

import heapq
def dij(S, T, g):
    # Dijkstra from S to T
    INF = 10**12
    dist = dd(inf)

    pq = []
    dist[S] = 0
    pq.append((0, S))
    heapq.heapify(pq)
    done = False
    while pq and not done:
        (nd, node) = heapq.heappop(pq)
        
        if node == T: done= True
        for (di, nn) in g[node]:
            alt = dist[node] + di
            if dist[nn] > alt:
                dist[nn] = alt
                heapq.heappush(pq, (dist[nn], nn))

    return dist[T]
    

def get_portals(grid):
    port= dd(list)
    for r in range(len(grid)-1):
        for c in range(len(grid[0])-1):
            if ord('A') <= ord(grid[r][c]) <= ord('Z'):
                if ord('A') <= ord(grid[r][c+1]) <= ord('Z'):
                    name = grid[r][c]+ grid[r][c+1]
                    if grid[r][c-1] == '.':
                        port[name].append((r, c-1))
                    elif grid[r][c+2] == '.':
                        port[name].append((r, c+2))
                if ord('A') <= ord(grid[r+1][c]) <= ord('Z'):
                    name = grid[r][c]+ grid[r+1][c]
                    if r > 0 and grid[r-1][c] == '.':
                        port[name].append((r-1, c))
                    elif grid[r+2][c] == '.':
                        port[name].append((r+2, c))
    return port


def get_sides(grid):
    start, goal = None, None
    inside = {}
    outside = {}
    for r in range(len(grid)-1):
        for c in range(len(grid[0])-1):
            if ord('A') <= ord(grid[r][c]) <= ord('Z'):
                if ord('A') <= ord(grid[r][c+1]) <= ord('Z'):
                    name = grid[r][c]+ grid[r][c+1]
                        
                    if grid[r][c-1] == '.':
                        if c == 0 or c == len(grid[0]) - 2:
                            outside[name] = r, c-1
                        else:
                            inside[name] = r, c -1

                    elif grid[r][c+2] == '.':
                        if c == 0 or c == len(grid[0]) - 2:
                            outside[name] = r, c+2
                        else:
                            inside[name] = r, c +2
                        
                if ord('A') <= ord(grid[r+1][c]) <= ord('Z'):
                    name = grid[r][c]+ grid[r+1][c]
                    if r > 0 and grid[r-1][c] == '.':
                        
                        if r == 0 or r == len(grid) - 2:
                            outside[name] = r-1, c
                        else:
                            inside[name] = r-1, c
                    elif grid[r+2][c] == '.':

                        if r == 0 or r == len(grid) - 2:
                            outside[name] = r+2, c
                        else:
                            inside[name] = r+2, c
    start = outside['AA']
    goal= outside['ZZ']
    del outside['AA']
    del outside['ZZ']
    
    return start, goal, inside, outside
           
def p1(v, log=False):
    return 0
    lines = v.split('\n')
    grid = []
    for line in lines:
        grid.append(line)
        
    portals = get_portals(grid)
    start = portals['AA'][0]
    goal = portals['ZZ'][0]
    poi = set()
    for label in portals.keys():
        for point in portals[label]:
            poi.add(point)
    g = dd(list)
    for point in poi:
        reach= bfs(point, grid, poi)
        g[point] = reach
    
    for label in portals.keys():
        if label != 'AA' and label!= 'ZZ':
            p1, p2 = portals[label]
            g[p1].append((1, p2))
            g[p2].append((1, p1))
    
    dT = dij(start, goal, g)            
    return dT

def p2(v, log=False):
    lines = v.split('\n')
    grid = []
    for line in lines:
        grid.append(line)
    start, goal, inside, outside = get_sides(grid)

    iset = {c:l for l,c in inside.items()}
    
    oset = {c:l for l,c in outside.items()}

    q= [(start, 0)]
    dG = bfs2((start, 0), (goal, 0), grid, iset, oset, inside, outside)

    return dG

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
