"""
https://adventofcode.com/2021/day/12
"""
from collections import defaultdict

edges = defaultdict(set)
vertices = set()
with open('day-12/input.txt', 'r') as fp:
    lines = fp.read().split('\n')
    for line in lines:
        a, b = line.split('-')
        vertices.add(a)
        vertices.add(b)
        if a != 'end' and b != 'start':
            edges[a].add(b)
        if a != 'start' and b != 'end':
            edges[b].add(a)

paths = set()
stack = [('start',)]
while stack:
    path = stack.pop(0)
    if path in paths:
        continue
    here = path[-1]
    for there in edges[here]:
        if there == 'end':
            paths.add(path + (there,))
        elif there not in path or there.isupper():
            stack.append(path + (there,))
print(f'problem 1: {len(paths)}')


paths = set()
stack = [(False, 'start')]
while stack:
    path = stack.pop(0)
    if path in paths:
        continue
    here = path[-1]
    for there in edges[here]:
        if there == 'end':
            paths.add(path[1:] + (there,))
        elif there not in path or there.isupper():
            stack.append(path + (there,))
        elif not path[0]:
            stack.append((True,) + path[1:] + (there,))
print(f'problem 2: {len(paths)}')
