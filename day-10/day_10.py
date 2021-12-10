"""
https://adventofcode.com/2021/day/10
"""

f = 'day-10/input.txt'

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
left = {'(', "{", '[', '<'}
right = {')', ']', '}', '>'}
r2l = {'>': '<', ')': '(', ']': '[', '}': '{'}


def p1(sequence):
    stack = list()
    for c in sequence:
        if c in right:  # close
            if r2l[c] == stack[-1]:  # valid
                stack.pop(-1)
            else:  # invalid
                return points[c], stack
        else:
            stack.append(c)
    # valid or incomplete
    return 0, stack


score = 0
with open(f, 'r') as fp:
    for line in fp.read().split('\n'):
        score += p1(line)[0]

print(f"problem 1: {score}")

l2r = {v: k for k, v in r2l.items()}
points = {')': 1, ']': 2, '}': 3, '>': 4}

scores = list()
with open(f, 'r') as fp:
    for line in fp.read().split('\n'):
        score, chars = p1(line)
        if not score and chars:  # incomplete
            p = 0
            for l in reversed(chars):
                p *= 5
                p += points[l2r[l]]
            scores.append(p)

print(f'problem 2: {list(sorted(scores))[len(scores)//2]}')
