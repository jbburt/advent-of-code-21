"""
https://adventofcode.com/2021/day/15
"""
import numpy as np

with open('day-15/input.txt', 'r') as fp:
    local = np.array([list(map(int, line)) for line in fp.read().split('\n')])

start = local[0, 0]
local[0, 0] = 0

deltas = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def main(grid):
    nrows, ncols = grid.shape
    unvisited = np.ones(grid.shape, dtype=bool)
    dist = np.array([np.inf] * nrows * ncols).reshape(grid.shape)
    dist[0, 0] = 0
    while unvisited.any():
        min_dist = dist[unvisited].min()
        v = tuple(x[0] for x in np.where(np.logical_and(unvisited, dist == min_dist)))
        unvisited[v] = False
        i, j = v
        for di, dj in deltas:
            u = (i + di, j + dj)
            if 0 <= u[0] <= nrows - 1 and 0 <= u[1] <= ncols - 1:
                if unvisited[u]:
                    dist_to_u = dist[v] + grid[u]
                    if dist_to_u < dist[u]:
                        dist[u] = dist_to_u
    return dist


d = main(local)
print(f'p1: {d[-1, -1]}')

nr, nc = local.shape
local2 = local.copy()
local2[0, 0] = start
local2 = np.tile(local2, (5, 5))

x = (np.arange(nr * 5) / nr).astype(int)
increment = np.add.outer(x, x).astype(int)

local2 += increment.astype(int)
local2 = np.mod(local2-1, 9)+1
local2[0, 0] = 0

d2 = main(local2)
print(f'p2: {d2[-1, -1]}')

