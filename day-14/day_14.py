"""
https://adventofcode.com/2021/day/14
"""

from itertools import product

with open('day-14/input.txt', 'r') as fp:
    lines = fp.read().split('\n')
    template = lines[0]
    rules = {k: v for (k, v) in map(lambda x: x.split(' -> '), lines[2:])}

# all unique characters
chars = set(template)
for k, v in rules.items():
    chars |= set(k).union(v)

# running tally of the number of each character pair
pairs = set(map(lambda x: "".join(x), list(product(chars, chars))))
npairs = {p: 0 for p in pairs}
for i in range(len(template) - 1):
    npairs[template[i:i + 2]] += 1


def solve(pair_count: dict) -> int:
    char_count = {c: 0 for c in chars}
    for k, v in pair_count.items():
        for c in k:
            char_count[c] += v
    for c in chars:
        start = sum(pair_count[p] for p in pairs if p[0] == c)
        end = sum(pair_count[p] for p in pairs if p[1] == c)
        char_count[c] -= min(start, end)
    _, n = zip(*char_count.items())
    return max(n) - min(n)


def simulate(n: int, pair_count: dict) -> dict:
    for _ in range(n):
        new_np = pair_count.copy()
        for pair, ct in pair_count.items():
            if pair in rules:
                new_np[pair[0] + rules[pair]] += ct
                new_np[rules[pair] + pair[1]] += ct
                new_np[pair] -= ct
        pair_count = new_np
    return pair_count


temp = simulate(10, npairs.copy())
print(f'p1: {solve(temp)}')
print(f'p2: {solve(simulate(30, temp))}')
