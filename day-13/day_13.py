"""
https://adventofcode.com/2021/day/12
"""

from collections import defaultdict
from collections import deque
import numpy as np
from scipy.signal import convolve2d
from itertools import accumulate


with open('day-13/input.txt', 'r') as fp:
    lines = fp.read().split('\n')
    points = list()
    instructions = list()
    for i, line in enumerate(lines):
        if not line:
            break
        points.append([int(i) for i in line.split(',')])
    for j in range(i+1, len(lines)):
        var, num = lines[j].split()[-1].split('=')
        instructions.append((var, int(num)))

# p1
new_pts = set()
for dim, value in instructions[:1]:
    for x, y in points:
        if dim == 'y':
            y = y if y <= value else value - (y-value)
        else:
            x = x if x <= value else value - (x-value)
        new_pts.add((x, y))
print(len(new_pts))

# p1
points = set(tuple(x) for x in points)
for dim, value in instructions:
    new_pts = set()
    for x, y in points:
        if dim == 'y':
            y = y if y <= value else value - (y-value)
        else:
            x = x if x <= value else value - (x-value)
        new_pts.add((x, y))
    points = new_pts
print(len(new_pts))

import matplotlib.pyplot as plt

x, y = list(zip(*list(points)))
plt.scatter(np.array(x), y)
plt.show()
