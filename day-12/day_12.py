"""
https://adventofcode.com/2021/day/12
"""
from collections import defaultdict
from collections import deque

edges = defaultdict(set)
isupper = dict()
with open('day-12/input.txt', 'r') as fp:
    for line in fp.read().split('\n'):
        a, b = line.split('-')
        for v in (a, b):
            if v not in isupper:
                isupper[v] = v.isupper()
        if a != 'end' and b != 'start':
            edges[a].add(b)
        if a != 'start' and b != 'end':
            edges[b].add(a)


npaths = 0
stack = deque([({'start'}, 'start')])
while stack:
    elements, last = stack.pop()
    for next_elem in edges[last]:
        if next_elem == 'end':
            npaths += 1
        elif isupper[next_elem] or next_elem not in elements:
            stack.append((elements.union({next_elem}), next_elem))
print(f'problem 1: {npaths}')

npaths = 0
stack = deque([(False, {'start'}, 'start')])
while stack:
    has_double, elements, last = stack.pop()
    for next_elem in edges[last]:
        if next_elem == 'end':
            npaths += 1
        elif isupper[next_elem] or next_elem not in elements:
            stack.append((has_double, elements.union({next_elem}), next_elem))
        elif not has_double:
            stack.append((True, elements.union({next_elem}), next_elem))
print(f'problem 2: {npaths}')
