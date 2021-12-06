"""
https://adventofcode.com/2021/day/6
"""

with open('day-06/input.txt', 'r') as fp:
    timer = list(map(int, fp.read().strip('\n').split(',')))


def simulate1(days):
    counts = {i: timer.count(i) for i in range(8)}
    for _ in range(days):
        new_counts = {age - 1: count for age, count in counts.items() if age}
        new_counts[8] = counts[0]
        new_counts[6] = new_counts.get(6, 0) + counts[0]
        counts = new_counts
    return sum(counts.values())


print(f'problem 1: {simulate1(80)}')
print(f'problem 2: {simulate1(256)}')


def simulate2(days):
    counts = [timer.count(i) for i in range(9)]
    idx_t0 = 0
    for _ in range(days):
        # add t0 fish to t7 bin, so when the t0 index shifts by 1,
        # there are n(t0) new fish in the t6 bin
        counts[(idx_t0 - 2) % 9] += counts[idx_t0]
        # shift the t0 index by one; note n(t0) rolls over to n(t8)
        idx_t0 = (idx_t0 + 1) % 9
    return sum(counts)


print(f'problem 1: {simulate2(80)}')
print(f'problem 2: {simulate2(256)}')
