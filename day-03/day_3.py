"""
https://adventofcode.com/2021/day/3
"""

# Read input
with open('day-03/input.txt', 'r') as fp:
    lines = fp.read().split('\n')

nc = len(lines[0])

# increment counter for a 1; decrement for a 0
count = {i: 0 for i in range(nc)}
for line in lines:
    for i, c in enumerate(line):
        if c == '0':
            count[i] -= 1
        else:
            count[i] += 1

# reconstruct binary string and convert to int (base 2)
gamma = int("".join(['0' if count[i] < 0 else '1' for i in range(nc)]), 2)
epsilon = int("".join(['0' if count[i] > 0 else '1' for i in range(nc)]), 2)
print(f'problem 1: {gamma * epsilon}')


# problem 2
def run(most_common):
    n = len(lines)
    inds = list(range(n))
    b = 0
    while n > 1:
        ints = [int(lines[i][b]) for i in inds]
        k = sum(ints)
        if k == (n / 2):
            target = 1 if most_common else 0
        else:
            op = '__gt__' if most_common else '__le__'
            target = int(getattr(k, op)(n // 2))
        inds = [inds[i] for i, x in enumerate(ints) if x == target]
        b += 1
        n = len(inds)
    return inds[0]


o2 = int(lines[run(most_common=True)], 2)
co2 = int(lines[run(most_common=False)], 2)
print(f'problem 2: {o2 * co2}')
