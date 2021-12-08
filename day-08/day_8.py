"""
https://adventofcode.com/2021/day/8
"""

from collections import defaultdict
from time import time

# from itertools import groupby

t1 = time()
with open('day-08/input.txt', 'r') as fp:
    signals, digits = zip(
        *[[x.split() for x in l.split(' | ')] for l in fp.read().split('\n')])

# nsegments -> digit for the four unique numbers
known = {2: '1', 4: '4', 3: '7', 7: '8'}
p1 = sum(sum(n in known for n in list(map(len, d))) for d in digits)


# problem 2


def anotb(str1, str2):
    return "".join(ci for ci in str1 if ci not in str2)


tot = 0
for s, d in zip(signals, digits):

    # sgroups = {k: list(v) for k, v in groupby(sorted(s, key=len), key=len)}
    sgroups = defaultdict(list)
    for c in s:
        sgroups[len(c)].append(c)

    # a is 7 not 1
    a = anotb(seven := sgroups[3][0], one := sgroups[2][0])

    # (c and f) are 7 not a
    cf = anotb(seven, a)

    # (b and d) are 4 not 1
    bd = anotb(sgroups[4][0], one)

    res = ''
    for string in d:
        if (n := len(string)) in known:
            res += known[n]
        elif n == 5:  # len(5): 2, 3, or 5
            if all(c in string for c in cf):  # len(5) and (c and f) -> 3
                res += '3'
            else:
                res += '5' if all(c in string for c in bd) else '2'
        else:  # len(6): 0, 6, or 9
            if all(c in string for c in cf):
                res += '9' if all(c in string for c in bd) else '0'
            else:
                res += '6'
    tot += int(res)

t = (time() - t1) * 1000

print(f'problem 1: {p1}')
print(f'problem 2: {tot}')
print(f'time: {round(t, 3)}ms')
