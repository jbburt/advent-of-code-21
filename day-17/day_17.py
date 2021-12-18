"""
https://adventofcode.com/2021/day/17
"""
from math import ceil
from math import sqrt
from re import match

with open('day-17/input.txt', 'r') as fp:
    pattern = f'target area: x=([0-9\-]*)..([0-9\-]*), y=([0-9\-]*)..([0-9\-]*)'
    xmin, xmax, ymin, ymax = map(int, match(pattern, fp.read().strip()).groups())

params = (xmin, xmax, ymin, ymax)


def simulate(x, y, vx, vy):
    return x + vx, y + vy, vx - int(vx and (1, -1)[vx < 0]), vy - 1


def tri(z):
    return int(z * (z + 1) / 2)


def is_perfectsquare(num):
    return int(sqrt(num)) ** 2 == num


def invtri(z):
    root = 1 + 8 * z
    if not is_perfectsquare(root):
        return None
    return int(sqrt(root) / 2 - 1 / 2)


def find_vx_bounds(xl, xr):
    lb = ceil(sqrt(1 + 8 * xl) / 2 - 0.5)
    rb = int(sqrt(1 + 8 * xr) / 2 - 0.5)
    return lb, rb


vxs = thats = list(set(find_vx_bounds(xmin, xmax)))
xhats = list(set([tri(t) for t in thats]))

vy_final = tri(abs(ymin))
print(f'p1: {vy_final + ymin}')

cutoff = find_vx_bounds(0, abs(ymin))[-1]
width = xmax - xmin + 1
# n = width * (abs(ymin)-cutoff)

dists = {i: i for i in range(0, abs(ymin)+1)}
# dists = {i: i for i in range(1, max(vxs)+1)}
for i in range(1, abs(ymin)+1):
    dists[i] += dists[i-1]

# n = 0
trajs = set()
vm = min(vxs)
for vx in range(min(vxs), xmax+1):
    vinit = vx
    x = t = 0
    points = list()
    while x < xmax and vx > 0:
        x += vx
        vx -= 1
        t += 1
        if xmin <= x <= xmax:
            points.append((vinit, x, t))
    # print(pairs)
    # _xs = [v for k, v in dists.items() if xmin <= dists[vx] + dists[vx-v] <= xmax]
    # print(vx, len(_xs))
    for vx_init, xint, t in points:
        for vy_init in range(ymin, -ymin):
            state = (0, 0, vx_init, vy_init)
            while state[0] <= xmax and state[1] >= ymin:
                state = simulate(*state)
                x, y = state[:2]
                if xmin <= x <= xmax and ymin <= y <= ymax:
                    # n += 1
                    trajs.add((vinit, vy_init))

print(f'p2: {len(trajs)}')
