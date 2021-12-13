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
        vertices |= {a, b}
        if a != 'end' and b != 'start':
            edges[a].add(b)
        if a != 'start' and b != 'end':
            edges[b].add(a)
isupper = {k: k.isupper() for k in vertices}

npaths = 0
stack = deque([({'start'}, 'start')])
while stack:
    small_caves, last = stack.pop()
    for next_elem in edges[last]:
        if next_elem == 'end':
            npaths += 1
        elif isupper[next_elem]:
            stack.append((small_caves, next_elem))
        elif next_elem not in small_caves:
            stack.append((small_caves | {next_elem}, next_elem))
print(f'problem 1: {npaths}')

npaths = 0
stack = deque([(False, {'start'}, 'start')])
while stack:
    has_double, small_caves, last = stack.pop()
    for next_elem in edges[last]:
        if next_elem == 'end':
            npaths += 1
        elif isupper[next_elem]:  # don't need to keep track of cave
            stack.append((has_double, small_caves, next_elem))
        elif next_elem not in small_caves:  # do need to keep track
            stack.append((has_double, small_caves | {next_elem}, next_elem))
        elif not has_double:  # change boolean flag
            stack.append((True, small_caves, next_elem))
print(f'problem 2: {npaths}')
