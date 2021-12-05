"""
https://adventofcode.com/2021/day/5
"""

from collections import defaultdict

# Read input
with open('day-05/input.txt', 'r') as fp:
    lines = fp.read().split('\n')

vline = defaultdict(set)
hline = defaultdict(set)
dline = []

points = set()

for line in lines:

    p1, p2 = line.split(' -> ')

    x1, y1 = (int(x) for x in p1.split(','))
    x2, y2 = (int(x) for x in p2.split(','))

    if x1 == x2:  # vertical line
        ys = vline[x1].intersection(range(min(y1, y2), max(y1, y2) + 1))
        points.update([(x1, y) for y in ys])
        vline[x1].update(range(min(y1, y2), max(y1, y2) + 1))

    elif y1 == y2:  # horizontal line
        xs = hline[y1].intersection(range(min(x1, x2), max(x1, x2) + 1))
        points.update([(x, y1) for x in xs])
        hline[y1].update(range(min(x1, x2), max(x1, x2) + 1))

    else:  # diagonal line
        dline.append(((x1, y1), (x2, y2)))

# Find points at which vertical and horizontal lines intersect
for x, ys in vline.items():
    for y, xs in hline.items():
        if x in xs and y in ys:
            points.add((x, y))

print(f'problem 1: {len(points)}')

# Find points at which diagonal line intersects other lines
all_dpoints = set()
for ((x1, y1), (x2, y2)) in dline:

    # compute points in the diagonal line
    xstep = 1 if x2 > x1 else -1
    ystep = 1 if y2 > y1 else -1
    dpoints = set(zip(range(x1, x2+xstep, xstep), range(y1, y2+ystep, ystep)))

    # check for intersections with vertical lines
    for x, ys in vline.items():
        intersection = set([(x, y) for y in ys]).intersection(dpoints)
        points.update(intersection)

    # check for intersections with horizontal lines
    for y, xs in hline.items():
        intersection = set([(x, y) for x in xs]).intersection(dpoints)
        points.update(intersection)

    # check for intersections with other diagonal lines
    intersection = all_dpoints.intersection(dpoints)
    points.update(intersection)
    all_dpoints.update(dpoints)

print(f'problem 2: {len(points)}')
