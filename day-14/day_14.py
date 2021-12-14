"""
https://adventofcode.com/2021/day/14
"""

from itertools import product

with open('day-14/input.txt', 'r') as fp:
    lines = fp.read().split('\n')
    template = lines[0]
    rules = dict()
    for line in lines[2:]:
        k, v = line.split(' -> ')
        rules[k] = v

# p1
tmp = template
for i in range(10):
    tmp = "".join(t + rules.get(t + tmp[i + 1], '') for i, t in enumerate(tmp[:-1])) + \
          tmp[-1]
counts = {c: tmp.count(c) for c in set(tmp)}
_, n = zip(*counts.items())
print(f'p1: {max(n) - min(n)}')

# p2
chars = set(template)
for k, v in rules.items():
    chars |= set(k)
    chars |= set(v)

pairs = set(map(lambda x: "".join(a for a in x), list(product(chars, chars))))
npairs = {p: 0 for p in pairs}
for i in range(len(template) - 1):
    npairs[template[i:i + 2]] += 1

for i in range(40):
    new_npairs = npairs.copy()
    for pair, n in npairs.items():
        if pair in rules:
            new_npairs[pair[0] + rules[pair]] += n
            new_npairs[rules[pair] + pair[1]] += n
            new_npairs[pair] -= n
    npairs = new_npairs

counts = {c: 0 for c in chars}
for k, v in npairs.items():
    for c in k:
        counts[c] += v

for c in chars:
    start = sum(npairs[p] for p in pairs if p[0] == c)
    end = sum(npairs[p] for p in pairs if p[1] == c)
    counts[c] -= min(start, end)
_, n = zip(*counts.items())
print(f'p2: {max(n) - min(n)}')

