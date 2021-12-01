"""
https://adventofcode.com/2021/day/1
"""

# Read input
f = 'day-01/input.txt'
with open(f, 'r') as fp:
    data = [int(x) for x in fp.read().split('\n')]

# Problem 1:
# How many measurements are larger than the previous measurement?
print(sum(b > a for b, a in zip(data[1:], data[:-1])))

# Problem 2:
# How many 3-sum measurements are larger than the previous 3-sum measurement?
print(sum(b > a for b, a in zip(data[3:], data[:-3])))

# (the trick was to notice that for each consecutive comparison, the (i-3)th
# element is dropped from the sum while the ith element is added, thus the
# 3-sum comparison is identical to a comparison between these two elements)
