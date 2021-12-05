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


def parametrize(_x1, _y1, _x2, _y2):
    dx = _x2 - _x1
    dy = _y2 - _y1
    _m = dy / dx
    _b = _y1 - _m * _x1
    return _m, _b


def find_intersection(_m, _b, _n, _c):
    xi = (_c - _b) / (_m - _n)
    yi = _m * xi + _b
    return xi, yi


def get_bounds(_x1, _y1, _x2, _y2):
    return (min(_x1, _x2), max(_x1, _x2)), (min(_y1, _y2), max(_y1, _y2))


def make_points(_x1, _y1, _x2, _y2):
    xstep = 1 if _x2 > _x1 else -1
    ystep = 1 if _y2 > _y1 else -1
    return zip(range(_x1, _x2 + xstep, xstep), range(_y1, _y2 + ystep, ystep))


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

params = {(p1, p2): parametrize(*p1, *p2) for p1, p2 in dline}
cache = dict()

# Find points at which diagonal line intersects other lines
for i, ((x1, y1), (x2, y2)) in enumerate(dline):

    # slope and intercept
    m, b = params[((x1, y1), (x2, y2))]

    # domain and range
    if ((x1, y1), (x2, y2)) in cache:
        xbds, ybds = cache[((x1, y1), (x2, y2))]
    else:
        xbds, ybds = get_bounds(x1, y1, x2, y2)
        cache[((x1, y1), (x2, y2))] = (xbds, ybds)

    # check for intersections with vertical lines
    for x, ys in vline.items():
        if xbds[0] <= x <= xbds[1]:
            yp = m * x + b
            if yp in ys:
                points.add((x, yp))

    # check for intersections with horizontal lines
    for y, xs in hline.items():
        if ybds[0] <= y <= ybds[1]:
            xp = (y - b) / m
            if xp in xs:
                points.add((xp, y))

    # check for intersections with other diagonal lines
    for ((x3, y3), (x4, y4)) in dline[i + 1:]:

        n, c = params[((x3, y3), (x4, y4))]

        # if lines not parallel
        if m != n:

            xint, yint = find_intersection(m, b, n, c)

            # apparently it doesn't count if the intersection is off the grid
            if xint != int(xint):
                continue

            # if intersection point lies within range & domain of line 1
            if (xbds[0] <= xint <= xbds[1]) and (ybds[0] <= yint <= ybds[1]):
                # check domain and range of line 2
                if ((x3, y3), (x4, y4)) in cache:
                    xbds2, ybds2 = cache[((x3, y3), (x4, y4))]
                else:
                    xbds2, ybds2 = get_bounds(x3, y3, x4, y4)
                    cache[((x3, y3), (x4, y4))] = (xbds2, ybds2)
                if (xbds2[0] <= xint <= xbds2[1]) and (ybds2[0] <= yint <= ybds2[1]):
                    # intersection point exists for the line segments
                    points.add((xint, yint))

        else:  # parallel lines
            if b == c:

                # check for non-overlapping segments
                if (max(x1, x2) < min(x3, x4)) or (max(x3, x4) < min(x1, x2)):
                    continue

                # compute the intersection
                points.update(
                    set(make_points(x1, y1, x2, y2)).intersection(
                        set(make_points(x3, y3, x4, y4)))
                )

print(f'problem 2: {len(points)}')
