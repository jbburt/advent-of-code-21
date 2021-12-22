"""
https://adventofcode.com/2021/day/21
"""

from itertools import product

import numpy as np

with open('day-21/input.txt', 'r') as f:
    lines = f.read().strip().split('\n')
    pos = [int(l.split(' ')[-1]) - 1 for l in lines]

init = pos.copy()
nroll = 0
die = 1
score = [0, 0]
currscore = 0
while True:
    nmove = 0
    for _ in range(3):
        nroll += 1
        nmove += die
        if die == 100:
            die = 1
        else:
            die += 1
    idx = currscore % 2
    pos[idx] = (pos[idx] + nmove) % 10
    score[idx] += (pos[idx] + 1)
    # print(pos, score)
    if score[currscore % 2] >= 1000:
        break
    currscore += 1

print(f'p1: {min(score) * nroll}')

# problem 2

combs = list(product([1, 2, 3], [1, 2, 3], [1, 2, 3]))
combs = [tuple(sorted(t)) for t in combs]
die_outcomes = dict.fromkeys([tuple(x) for x in set(combs)])
for comb in set(combs):
    die_outcomes[comb] = combs.count(comb)
# or just use fact that n_outcomes = 3 * len(set(comb))...

# calculate the distribution of possible outcomes on a given step
# the number of places a player moves on any turn is 3, 4, 5, 6, 7, 8, or 9
nmoves = {i: 0 for i in range(3, 10)}
for triplet, n_score in die_outcomes.items():
    nmoves[sum(triplet)] += n_score
# each turn (set of 3 rolls) therefore spawns 27 universes in proportion to the
# number of ways each outcome can occur:
distro = np.empty(10).astype(int)
for nmove, n_univ in nmoves.items():
    distro[nmove] += n_univ

# player1, score1, player2, score2
count = np.zeros((10, 22, 10, 22)).astype(int)

# initialize with no score at initial positions
count[init[0], 0, init[1], 0] = 1

np1 = np2 = 0  # scores
i = 0
while count.any():
    i += 1
    player = (i + 1) % 2
    tmp = np.zeros(count.shape).astype(int)
    for currpos, currscore in list(product(range(10), range(22))):
        # player rolls 3x with these possible outcomes -- number represents the
        # number of new universes, and index represents position on the board
        outcomes = np.roll(distro, currpos)
        for newpos, noutcomes in enumerate(outcomes):
            newscore = currscore + (newpos + 1)
            if newscore >= 21:  # current player wins
                nwin = count[currpos, currscore].sum() * noutcomes
                if player:
                    np2 += nwin
                else:
                    np1 += nwin
            else:  # update the multiverse ledger
                tmp[newpos, newscore] += count[currpos, currscore] * noutcomes
    # swap players to change who is currently rolling the die
    count = tmp
    count = np.swapaxes(count, 0, 2)
    count = np.swapaxes(count, 1, 3)

print(f'p2: {max(np1, np2)}')
