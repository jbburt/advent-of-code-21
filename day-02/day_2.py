"""
https://adventofcode.com/2021/day/2
"""


# Read input
f = 'day-02/input.txt'
with open(f, 'r') as fp:
    lines = list(map(lambda line: line.split(' '), fp.read().split('\n')))

depth1 = depth2 = hp = 0
for direction, magnitude in lines:
    if direction == 'up':
        depth1 -= int(magnitude)
    elif direction == 'down':
        depth1 += int(magnitude)
    else:
        hp += int(magnitude)
        depth2 += depth1 * int(magnitude)

print(f'problem 1: {hp * depth1}')
print(f'problem 2: {hp * depth2}')
