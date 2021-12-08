"""
https://adventofcode.com/2021/day/7
"""

from itertools import accumulate

with open('day-07/input.txt', 'r') as fp:
    pos = list(sorted(map(int, fp.read().strip('\n').split(','))))

dists = [abs(x - pos[int(len(pos) / 2)]) for x in pos]
print(f'problem 1: {sum(abs(d) for d in dists)}')

cache = list(accumulate(range(max(pos) + 1)))
min_fuel = float('inf')
for i in range(max(pos)):
    min_fuel = min(min_fuel, sum([cache[abs(p - i)] for p in pos]))
print(f'problem 2: {min_fuel}')
