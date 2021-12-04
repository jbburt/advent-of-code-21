"""
https://adventofcode.com/2021/day/4
"""
import numpy as np


def load():
    _boards = list()
    with open('day-04/input.txt', 'r') as fp:
        _nums = list(map(int, fp.readline().rstrip('\n').split(',')))
        while _ := fp.readline():
            _boards.append(
                [list(map(int, fp.readline().rstrip('\n').split())) for _ in range(5)]
            )
    return _nums, _boards


# ############
# Pythonic way
# ############

# load bingo numbers and bingo board
nums, boards = load()

# all possible winning combinations
rows = [line for board in boards for line in board]
cols = [[line[i] for line in board] for board in boards for i in range(5)]
sets = [set(line) for line in rows + cols]

# find idx of winning board (ix)
n = 4
while n := n + 1:
    if any(set(nums[:n]).issuperset(s) for s in sets):
        ix = ([set(nums[:n]).issuperset(s) for s in sets].index(True) % len(rows)) // 5
        break

res = nums[n - 1] * sum(
    set([x for line in boards[ix] for x in line]).difference(set(nums[:n]))
)
print(f"problem 1: {res}")

# problem 2: find last winning board
remaining = set(range(len(boards)))
remaining.remove(ix)
combos = dict.fromkeys(remaining)
for ib in combos:
    combos[ib] = rows[5 * ib:5 * ib + 5] + cols[5 * ib:5 * ib + 5]

while (n := n + 1) and remaining:
    remove = [board for board in combos if any(
        set(nums[:n]).issuperset(s) for s in combos[board])]
    for board in remove:
        del combos[board]
        remaining.remove(board)

res = nums[n - 2] * sum(
    set([x for line in boards[board] for x in line]).difference(set(nums[:n - 1]))
)
print(f"problem 2: {res}")

# ###############
# Numpythonic way
# ###############

nums, boards = load()
boards = np.array(boards)

# find idx of winning board (ix)
for n, num in enumerate(nums):
    boards[boards == num] = 0
    if not boards.sum(1).all():
        ix = np.where(boards.sum(1).all(1) == 0)[0][0]
        break
    elif not boards.sum(2).all():
        ix = np.where(boards.sum(2).all(1) == 0)[0][0]
        break

print(f"problem 1: {num * boards[ix].sum()}")

# problem 2: find last winning board
remaining = set(range(len(boards)))
remaining.remove(ix)

while (n := n + 1) and remaining:
    boards[boards == nums[n]] = 0
    winners = np.where((~boards.sum(1).all(1)) | (~boards.sum(2).all(1)))[0]
    remove = set(winners).intersection(remaining)
    for r in remove:
        remaining.discard(r)

res = nums[n - 1] * boards[r].sum()
print(f"problem 2: {res}")