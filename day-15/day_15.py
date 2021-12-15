"""
https://adventofcode.com/2021/day/15
"""
import heapq as hq
import itertools
from time import time

import numpy as np

t0 = time()

with open('day-15/input.txt', 'r') as fp:
    local = np.array([list(map(int, line)) for line in fp.read().split('\n')])

start = local[0, 0]
local[0, 0] = 0

deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]

nr, nc = local.shape

pairs = set(list(itertools.product(range(nr), range(nc))))
dist = {point: float('inf') for point in pairs}
dist[(0, 0)] = 0
d = [(0, (0, 0))] + [(float('inf'), pair) for pair in pairs]

d = list(sorted(d, key=lambda z: z[0]))
hq.heapify(d)
unvisited = pairs.copy()
while unvisited:
    dist_to_v, v = hq.heappop(d)
    unvisited.remove(v)
    i, j = v
    for di, dj in deltas:
        u = (i + di, j + dj)
        if u in unvisited and 0 <= u[0] <= nr - 1 and 0 <= u[1] <= nc - 1:
            dist_to_u = dist[v] + local[u]
            if dist_to_u < dist[u]:
                dist[u] = dist_to_u
                hq.heappush(d, (dist[u], u))

print('p1:', dist[(nr - 1, nc - 1)])

local2 = local.copy()
local2[0, 0] = start
local2 = np.tile(local2, (5, 5))

x = (np.arange(nr * 5) / nr).astype(int)
increment = np.add.outer(x, x).astype(int)

local2 += increment.astype(int)
local2 = np.mod(local2 - 1, 9) + 1

nr, nc = local2.shape

pairs = set(list(itertools.product(range(nr), range(nc))))
dist = {point: float('inf') for point in pairs}
dist[(0, 0)] = 0
d = [(0, (0, 0))] + [(float('inf'), pair) for pair in pairs]

d = list(sorted(d, key=lambda z: z[0]))
hq.heapify(d)
unvisited = pairs.copy()

while unvisited:
    dist_to_v, v = hq.heappop(d)
    unvisited.remove(v)
    i, j = v
    for di, dj in deltas:
        u = (i + di, j + dj)
        if u in unvisited and 0 <= u[0] <= nr - 1 and 0 <= u[1] <= nc - 1:
            dist_to_u = dist[v] + local2[u]
            if dist_to_u < dist[u]:
                dist[u] = dist_to_u
                hq.heappush(d, (dist[u], u))

print('p2:', dist[(nr - 1, nc - 1)])
print('time:', time() - t0)
