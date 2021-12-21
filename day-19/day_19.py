"""
https://adventofcode.com/2021/day/19
"""

from scipy.spatial.transform import Rotation
from collections import deque
import numpy as np
import re

data = dict()
with open('day-19/input.txt', 'r') as fp:
    lines = fp.read().strip().split('\n')
    for line in lines:
        z = re.match(r'--- scanner ([0-9]+) ---', line)
        if z:
            scanner = int(z.groups()[0])
            data[scanner] = []
        elif line:
            data[scanner].append(list(map(int, line.split(','))))
        else:
            continue

assert np.allclose(np.array(np.sort(list(data.keys()))), np.arange(len(data)))

locs = [np.array(data[i]) for i in range(len(data))]


# rotation matrices
rot = Rotation.from_matrix(np.ones(9).reshape(3, 3))
rotmats = rot.create_group('O').as_matrix().astype('int64')


def toset(arr):
    return set(tuple(b) for b in arr)


def compare(s1):
    scanner1 = locs[s1]
    for b0 in scanner0:
        ref = scanner0 - b0
        refset = toset(ref)
        for b1 in scanner1:
            for ir, r in enumerate(rotmats):
                b1_ref = scanner1 - b1
                brot = b1_ref.dot(r).astype(int)
                noverlap = len(toset(brot).intersection(refset))
                if noverlap >= 12:
                    b1rot = b1.dot(r)
                    d10_ref = b0 - b1rot  # r from s0 to s1 in ref frame
                    return True, d10_ref, d10_ref + scanner1.dot(r)
    return False, None, None


nsensor = len(locs)
scanner0 = locs.pop(0)
known_beacons = set(tuple(x) for x in scanner0)
unmatched = deque(list(range(0, nsensor-1)))

rvecs = list()
while unmatched:
    print(unmatched)
    idx = unmatched.popleft()
    success, rvec, vectors = compare(idx)
    if not success:
        unmatched.append(idx)
    else:
        rvecs.append(rvec)
        for vec in vectors:
            known_beacons.add(tuple([int(i) for i in vec]))
        scanner0 = np.array(list(iter(known_beacons)))

print(f'p1: {len(known_beacons)}')


def mdist(v):
    return np.sum(np.abs(v))


maxdist = max(mdist(v) for v in rvecs)
for i in range(len(rvecs)):
    for j in range(i, len(rvecs)):
        maxdist = max(maxdist, mdist(rvecs[i]-rvecs[j]))
print(f'p2: {maxdist}')
