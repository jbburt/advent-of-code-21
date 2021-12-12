"""
https://adventofcode.com/2021/day/12
"""
from collections import defaultdict
from collections import deque

edges = defaultdict(set)
with open('day-12/input.txt', 'r') as fp:
    for line in fp.read().split('\n'):
        a, b = line.split('-')
        if a != 'end' and b != 'start':
            edges[a].add(b)
        if a != 'start' and b != 'end':
            edges[b].add(a)

npaths = 0
stack = deque([('start',)])
while stack:
    path = stack.pop()
    for there in edges[path[-1]]:
        if there == 'end':
            npaths += 1
        elif there not in path or there.isupper():
            stack.append(path + (there,))
print(f'problem 1: {npaths}')

npaths = 0
stack = deque([(False, 'start')])
while stack:
    path = stack.pop()
    for there in edges[path[-1]]:
        if there == 'end':
            npaths += 1
        elif there.isupper() or there not in path:
            stack.append(path + (there,))
        elif not path[0]:
            stack.append((True,) + path[1:] + (there,))
print(f'problem 2: {npaths}')
