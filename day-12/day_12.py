"""
https://adventofcode.com/2021/day/12
"""
from collections import defaultdict
from collections import deque

edges = defaultdict(set)
vertices = set()
with open('day-12/input.txt', 'r') as fp:
    for line in fp.read().split('\n'):
        a, b = line.split('-')
        vertices.add(a)
        vertices.add(b)
        if a != 'end' and b != 'start':
            edges[a].add(b)
        if a != 'start' and b != 'end':
            edges[b].add(a)
isupper = {k: k.isupper() for k in vertices}

npaths = 0
stack = deque([({'start'}, 'start')])
while stack:
    path, last = stack.pop()
    for there in edges[last]:
        if there == 'end':
            npaths += 1
        elif isupper[there] or there not in path:
            stack.append((path.union({there}), there))
print(f'problem 1: {npaths}')

npaths = 0
stack = deque([(False, {'start'}, 'start')])
while stack:
    has_double, path, last = stack.pop()
    for there in edges[last]:
        if there == 'end':
            npaths += 1
        elif isupper[there] or there not in path:
            stack.append((has_double, path.union({there}), there))
        elif not has_double:
            stack.append((True, path.union({there}), there))
print(f'problem 2: {npaths}')
